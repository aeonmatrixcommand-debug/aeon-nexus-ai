"""Single-host durable SQLite audit adapter (stdlib only).

Host provisioning: SQLiteAudit(path, create=True) creates a NEW database only;
normal/restart use: SQLiteAudit(path). Missing/malformed state is never recreated.
Each append uses BEGIN IMMEDIATE, DELETE journaling and synchronous=EXTRA, and
acknowledges only after COMMIT. A process crash rolls back incomplete writes.

Assumes a reliable local filesystem with working SQLite locks/fsync. No network
filesystem, replication, WORM, tamper-proofing, external anchoring, or protection
against an administrator rewriting/restoring the entire database is provided.
Hash-chain validation detects corruption, not an independently anchored history.
Full history is checked on every read/append: conservative O(n), not high-volume
distributed storage. Backups, filesystem permissions and retention are host duties.
"""

from dataclasses import replace
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sqlite3
from uuid import uuid4

from src.governance.audit_event import (
    AuditError, AuditEvent, AuditIntegrityError, AuditReceipt, GENESIS_DIGEST,
    IdempotencyConflict, canonical_json, sha256,
)
from src.governance.audit_sink import DurableAuditSink


SCHEMA = {
    "records": "CREATE TABLE records (sequence INTEGER PRIMARY KEY, payload TEXT NOT NULL, digest TEXT NOT NULL, key_hash TEXT NOT NULL UNIQUE)",
    "head": "CREATE TABLE head (id INTEGER PRIMARY KEY CHECK(id=1), version INTEGER NOT NULL, sequence INTEGER NOT NULL, digest TEXT NOT NULL)",
}


class SQLiteAudit(DurableAuditSink):
    def __init__(self, path, *, create=False, timeout=5.0):
        self.path = Path(path).absolute()
        self.timeout = timeout
        try:
            if create:
                # Explicit, exclusive provisioning; no recovery by truncation.
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                os.close(fd)
                with self._connection() as db:
                    db.execute("BEGIN IMMEDIATE")
                    for sql in SCHEMA.values():
                        db.execute(sql)
                    db.execute("INSERT INTO head VALUES (1, 1, 0, ?)", (GENESIS_DIGEST,))
                    db.commit()
                # Persist directory entry creation as well as database contents.
                fd = os.open(self.path.parent, os.O_RDONLY)
                try:
                    os.fsync(fd)
                finally:
                    os.close(fd)
            self.history()
        except AuditError:
            raise
        except Exception:
            raise AuditError("audit_storage_unavailable") from None

    def _connection(self):
        # mode=rw prevents a missing production database becoming an empty ledger.
        db = sqlite3.connect(self.path.as_uri() + "?mode=rw", uri=True,
                             timeout=self.timeout, isolation_level=None)
        try:
            db.execute("PRAGMA trusted_schema=OFF")
            if db.execute("PRAGMA journal_mode").fetchone()[0] != "delete":
                raise AuditIntegrityError("unsupported_audit_journal")
            db.execute("PRAGMA synchronous=EXTRA")
            if db.execute("PRAGMA synchronous").fetchone()[0] != 3:
                raise AuditError("audit_sync_unavailable")
            return _ClosingConnection(db)
        except Exception:
            db.close()
            raise

    @staticmethod
    def _verify(db):
        try:
            if db.execute("PRAGMA quick_check").fetchall() != [("ok",)]:
                raise ValueError()
            schema = dict(db.execute(
                "SELECT name, sql FROM sqlite_master WHERE name NOT LIKE 'sqlite_%'"
            ).fetchall())
            if schema != SCHEMA:
                raise ValueError()
            rows = db.execute("SELECT sequence, payload, digest, key_hash FROM records ORDER BY sequence").fetchall()
            previous = GENESIS_DIGEST
            records = []
            seen_keys, seen_ids = set(), set()
            for expected, (sequence, payload, digest, key_hash) in enumerate(rows, 1):
                record = json.loads(payload)
                if (sequence != expected or canonical_json(record) != payload
                        or sha256(payload) != digest
                        or set(record) != {"version", "sequence", "audit_id", "timestamp",
                                           "previous_digest", "idempotency_digest", "event"}
                        # JSON booleans/floats compare equal to Python integers,
                        # but are not valid versioned envelope integer fields.
                        or type(record["version"]) is not int or record["version"] != 1
                        or type(record["sequence"]) is not int or record["sequence"] != sequence
                        or record["previous_digest"] != previous
                        or record["idempotency_digest"] != key_hash
                        or type(key_hash) is not str or not re.fullmatch("[0-9a-f]{64}", key_hash)
                        or key_hash in seen_keys or record["audit_id"] in seen_ids
                        or not re.fullmatch("[0-9a-f]{32}", record["audit_id"])
                        or datetime.fromisoformat(record["timestamp"]).utcoffset() is None
                        or AuditEvent.from_mapping(record["event"]).to_dict() != record["event"]):
                    raise ValueError()
                seen_keys.add(key_hash)
                seen_ids.add(record["audit_id"])
                previous = digest
                records.append({**record, "digest": digest})
            if db.execute("SELECT id, version, sequence, digest FROM head").fetchall() != [
                    (1, 1, len(rows), previous)]:
                raise ValueError()
            return records
        except Exception:
            raise AuditIntegrityError("audit_integrity_failed") from None

    @staticmethod
    def _receipt(record):
        return AuditReceipt(record["audit_id"], record["sequence"], record["digest"],
                            record["previous_digest"], durable=True)

    def append(self, event: dict, *, idempotency_key: str) -> AuditReceipt:
        snapshot = AuditEvent.from_mapping(event)
        if type(idempotency_key) is not str or not idempotency_key or len(idempotency_key) > 256:
            raise AuditError("invalid_idempotency_key")
        # Persist only the hash of the host key, never potentially sensitive text.
        try:
            key_hash = sha256(idempotency_key)
        except Exception:
            raise AuditError("invalid_idempotency_key") from None
        try:
            with self._connection() as db:
                db.execute("BEGIN IMMEDIATE")
                records = self._verify(db)
                for record in records:
                    if record["idempotency_digest"] == key_hash:
                        if canonical_json(record["event"]) != snapshot.canonical:
                            raise IdempotencyConflict("idempotency_conflict")
                        receipt = replace(self._receipt(record), duplicate=True)
                        db.commit()
                        return receipt
                record = {
                    "version": 1, "sequence": len(records) + 1, "audit_id": uuid4().hex,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "previous_digest": records[-1]["digest"] if records else GENESIS_DIGEST,
                    "idempotency_digest": key_hash, "event": snapshot.to_dict(),
                }
                payload = canonical_json(record)
                digest = sha256(payload)
                db.execute("INSERT INTO records VALUES (?, ?, ?, ?)",
                           (record["sequence"], payload, digest, key_hash))
                db.execute("UPDATE head SET sequence=?, digest=? WHERE id=1",
                           (record["sequence"], digest))
                db.commit()
                # No receipt exists before successful commit acknowledgment.
                return self._receipt({**record, "digest": digest})
        except AuditError:
            raise
        except Exception:
            raise AuditError("audit_append_failed") from None

    def history(self) -> list[dict]:
        try:
            with self._connection() as db:
                db.execute("BEGIN")
                records = self._verify(db)
                db.commit()
                return records
        except AuditError:
            raise
        except Exception:
            raise AuditError("audit_read_failed") from None


class _ClosingConnection:
    """Unlike sqlite3's context manager, always closes the connection."""
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        return self.db

    def __exit__(self, *_):
        try:
            if self.db.in_transaction:
                self.db.rollback()
        finally:
            self.db.close()
