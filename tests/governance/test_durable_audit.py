"""Local-filesystem persistence contract tests; no providers or network."""

from concurrent.futures import ThreadPoolExecutor
import json
import os
import sqlite3
import subprocess
import sys

import pytest

from src.governance.audit_event import (
    AuditError, AuditEvent, AuditIntegrityError, GENESIS_DIGEST,
    IdempotencyConflict, canonical_json, sha256,
)
from src.governance.sqlite_audit import SQLiteAudit


def event():
    return {"stage": "evidence", "reason": "invalid_evidence", "status": "NO_DECISION",
            "executed": False, "execution_authorized": False, "evidence_ids": ["a" * 32]}


def run_child(code, *args):
    return subprocess.run([sys.executable, "-B", "-c", code, *map(str, args)],
                          capture_output=True, text=True, timeout=20,
                          env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})


def test_restart_recovery_and_sequence(tmp_path):
    path = tmp_path / "audit.db"
    first = SQLiteAudit(path, create=True).append(event(), idempotency_key="first")
    child = run_child("""
import sys
from src.governance.sqlite_audit import SQLiteAudit
sink = SQLiteAudit(sys.argv[1])
assert sink.history()[0]['sequence'] == 1
receipt = sink.append(sink.history()[0]['event'], idempotency_key='second')
assert receipt.sequence == 2 and receipt.durable
""", path)
    assert child.returncode == 0, child.stderr
    records = SQLiteAudit(path).history()
    assert [r["sequence"] for r in records] == [1, 2]
    assert records[1]["previous_digest"] == first.digest


def test_duplicate_key_returns_original_receipt_without_append(tmp_path):
    path = tmp_path / "audit.db"
    first = SQLiteAudit(path, create=True).append(event(), idempotency_key="retry")
    sink = SQLiteAudit(path)
    duplicate = sink.append(dict(reversed(list(event().items()))), idempotency_key="retry")
    assert duplicate.duplicate and duplicate.durable
    assert (duplicate.audit_id, duplicate.sequence, duplicate.digest) == (
        first.audit_id, first.sequence, first.digest)
    assert len(sink.history()) == 1


def test_conflicting_duplicate_key_is_rejected(tmp_path):
    sink = SQLiteAudit(tmp_path / "audit.db", create=True)
    sink.append(event(), idempotency_key="retry")
    with pytest.raises(IdempotencyConflict, match="^idempotency_conflict$"):
        sink.append({**event(), "reason": "egress_denied"}, idempotency_key="retry")
    assert len(sink.history()) == 1


def test_concurrent_process_writers_and_duplicate_detection(tmp_path):
    path = tmp_path / "audit.db"
    SQLiteAudit(path, create=True)
    code = """
import json, sys
from src.governance.sqlite_audit import SQLiteAudit
sink = SQLiteAudit(sys.argv[1], timeout=10)
event = json.loads(sys.argv[2])
sink.append(event, idempotency_key='shared')
for n in range(3):
    sink.append(event, idempotency_key=sys.argv[3] + str(n))
"""
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda i: run_child(code, path, json.dumps(event()), str(i)), range(4)))
    assert all(r.returncode == 0 for r in results), [r.stderr for r in results]
    records = SQLiteAudit(path).history()
    assert [r["sequence"] for r in records] == list(range(1, 14))
    assert len({r["idempotency_digest"] for r in records}) == 13


@pytest.mark.parametrize("crash", ["before_commit", "after_commit"])
def test_interrupted_append_recovery_and_retry(tmp_path, crash):
    path = tmp_path / "audit.db"
    SQLiteAudit(path, create=True).append(event(), idempotency_key="baseline")
    code = """
import json, os, sys
from src.governance.sqlite_audit import SQLiteAudit
sink = SQLiteAudit(sys.argv[1])
original = sink._connection
class CrashContext:
    def __enter__(self):
        self.context = original()
        self.db = self.context.__enter__()
        return self
    def execute(self, *args): return self.db.execute(*args)
    def commit(self):
        if sys.argv[3] == 'after_commit': self.db.commit()
        os._exit(73)
    def __exit__(self, *args): return self.context.__exit__(*args)
sink._connection = CrashContext
sink.append(json.loads(sys.argv[2]), idempotency_key='interrupted')
raise AssertionError('receipt must not have reached caller')
"""
    child = run_child(code, path, json.dumps(event()), crash)
    assert child.returncode == 73, child.stderr
    recovered = SQLiteAudit(path)
    assert len(recovered.history()) == (1 if crash == "before_commit" else 2)
    receipt = recovered.append(event(), idempotency_key="interrupted")
    assert receipt.sequence == 2
    assert receipt.duplicate == (crash == "after_commit")
    assert len(recovered.history()) == 2


def test_hash_chain_and_canonical_encoding(tmp_path):
    sink = SQLiteAudit(tmp_path / "audit.db", create=True)
    for n in range(3):
        sink.append(event(), idempotency_key=str(n))
    previous = GENESIS_DIGEST
    for record in sink.history():
        digest = record.pop("digest")
        assert record["previous_digest"] == previous
        assert sha256(canonical_json(record)) == digest
        previous = digest
    assert canonical_json({"b": 1, "a": 2}) == '{"a":2,"b":1}'
    with pytest.raises(ValueError):
        canonical_json({"value": float("nan")})


@pytest.mark.parametrize("corruption", ["event", "digest", "sequence", "head", "deleted_tail", "schema"])
def test_corrupted_record_detection_on_read_and_append(tmp_path, corruption):
    path = tmp_path / "audit.db"
    sink = SQLiteAudit(path, create=True)
    sink.append(event(), idempotency_key="one")
    sql = {
        "event": "UPDATE records SET payload='{}'",
        "digest": "UPDATE records SET digest='bad'",
        "sequence": "UPDATE records SET sequence=9",
        "head": "UPDATE head SET digest='bad'",
        "deleted_tail": "DELETE FROM records",
        "schema": "CREATE TABLE unexpected (data TEXT)",
    }[corruption]
    with sqlite3.connect(path) as db:
        db.execute(sql)
    for operation in (sink.history, lambda: sink.append(event(), idempotency_key="two"),
                      lambda: SQLiteAudit(path)):
        with pytest.raises(AuditIntegrityError):
            operation()


@pytest.mark.parametrize("contents", [b"", b"not a sqlite database"])
def test_malformed_existing_state_never_reinitialized(tmp_path, contents):
    path = tmp_path / "audit.db"
    path.write_bytes(contents)
    with pytest.raises(AuditError):
        SQLiteAudit(path)
    assert path.read_bytes() == contents
    with pytest.raises(AuditError):
        SQLiteAudit(path, create=True)
    assert path.read_bytes() == contents


def test_missing_database_is_not_silently_created(tmp_path):
    path = tmp_path / "missing.db"
    with pytest.raises(AuditError):
        SQLiteAudit(path)
    assert not path.exists()


def test_durable_mutation_isolation(tmp_path):
    sink = SQLiteAudit(tmp_path / "audit.db", create=True)
    original = event()
    snapshot = AuditEvent.from_mapping(original)
    sink.append(original, idempotency_key="one")
    original["evidence_ids"].append("b" * 32)
    history = sink.history()
    history[0]["event"]["evidence_ids"].clear()
    assert sink.history()[0]["event"]["evidence_ids"] == ["a" * 32]
    assert snapshot.to_dict()["evidence_ids"] == ["a" * 32]


def test_secret_allowlist_and_idempotency_key_hash(tmp_path):
    path = tmp_path / "audit.db"
    sink = SQLiteAudit(path, create=True)
    secret = "fixture-secret-credential-private-prompt"
    supplied = {**event(), "api_key": secret, "credentials": {"password": secret},
                "prompt": secret, "request": secret, "response": secret}
    sink.append(supplied, idempotency_key=secret)
    assert sink.history()[0]["event"] == event()
    assert secret.encode() not in path.read_bytes()
    assert secret not in json.dumps(sink.history())
    with pytest.raises(AuditError, match="^invalid_audit_event$"):
        sink.append({**event(), "reason": secret}, idempotency_key="two")
    assert len(sink.history()) == 1


def test_lock_timeout_fails_without_sequence_gap(tmp_path):
    path = tmp_path / "audit.db"
    sink = SQLiteAudit(path, create=True, timeout=0.01)
    with sqlite3.connect(path) as locked:
        locked.execute("BEGIN IMMEDIATE")
        with pytest.raises(AuditError, match="^audit_append_failed$"):
            sink.append(event(), idempotency_key="one")
    assert sink.append(event(), idempotency_key="one").sequence == 1


def test_broken_chain_detected_even_with_recomputed_record_digest(tmp_path):
    path = tmp_path / "audit.db"
    sink = SQLiteAudit(path, create=True)
    sink.append(event(), idempotency_key="one")
    sink.append(event(), idempotency_key="two")
    with sqlite3.connect(path) as db:
        record = json.loads(db.execute("SELECT payload FROM records WHERE sequence=2").fetchone()[0])
        record["previous_digest"] = GENESIS_DIGEST
        payload = canonical_json(record)
        digest = sha256(payload)
        db.execute("UPDATE records SET payload=?, digest=? WHERE sequence=2", (payload, digest))
        db.execute("UPDATE head SET digest=?", (digest,))
    with pytest.raises(AuditIntegrityError):
        sink.history()


@pytest.mark.parametrize("field", ["version", "sequence"])
@pytest.mark.parametrize("value", [True, 1.0])
def test_non_integer_envelope_rejected_even_with_valid_hash(tmp_path, field, value):
    path = tmp_path / "audit.db"
    sink = SQLiteAudit(path, create=True)
    sink.append(event(), idempotency_key="one")
    with sqlite3.connect(path) as db:
        record = json.loads(db.execute("SELECT payload FROM records").fetchone()[0])
        record[field] = value
        payload = canonical_json(record)
        digest = sha256(payload)
        db.execute("UPDATE records SET payload=?, digest=?", (payload, digest))
        db.execute("UPDATE head SET digest=?", (digest,))
    # Consistent hashes cannot substitute for validating the envelope schema.
    before = path.read_bytes()
    for operation in (sink.history, lambda: SQLiteAudit(path),
                      lambda: sink.append(event(), idempotency_key="two")):
        with pytest.raises(AuditIntegrityError, match="^audit_integrity_failed$"):
            operation()
    assert path.read_bytes() == before
