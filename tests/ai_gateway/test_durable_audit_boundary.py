from datetime import datetime, timezone
import json
import sqlite3
from types import SimpleNamespace

import pytest

from ai_gateway.audit import AuditTrail
from ai_gateway.evidence import EvidenceError, EvidenceGate, EvidenceSource
from ai_gateway.governed_analysis import CapabilityCategory, CapabilityPolicy, GovernedAnalysis
from ai_gateway.router import ProviderRouter
from src.governance.audit_event import AuditError, AuditReceipt
from src.governance.audit_sink import DurableAuditSink
from src.governance.immutable_audit import ImmutableAudit
from src.governance.sqlite_audit import SQLiteAudit


def setup_boundary(tmp_path, *, sink=None):
    path = tmp_path / "audit.db"
    sink = SQLiteAudit(path, create=True) if sink is None else sink
    audit = AuditTrail(sink, mode="production")
    source = EvidenceSource(lambda: {"observed_at": datetime.now(timezone.utc),
                                    "values": {"distance": 10}},
                            frozenset({"distance"}), frozenset({"distance"}), "PUBLIC")
    gate = EvidenceGate({"source": source}, audit=audit, audit_mode="production")
    calls = []
    def generate(payload):
        calls.append(json.loads(payload))
        return {"summary": "Advisory only", "evidence_ids": [calls[-1]["evidence"][0]["evidence_id"]]}
    router = ProviderRouter()
    router.register("fake", SimpleNamespace(generate=generate))
    boundary = GovernedAnalysis(router=router, provider_name="fake", evidence=gate,
        capabilities={"analysis": CapabilityPolicy(frozenset({"source"}), CapabilityCategory.READ_ONLY)},
        audit=audit, audit_mode="production")
    request = {"capability": "analysis", "evidence_ids": [gate.collect("source")]}
    return boundary, request, calls, sink, gate


def test_durable_ack_before_release(tmp_path):
    boundary, request, calls, sink, _ = setup_boundary(tmp_path)
    result = boundary.analyze(request)
    recovered = SQLiteAudit(sink.path).history()
    assert result["status"] == "PROPOSED"
    assert result["audit_id"] == recovered[0]["audit_id"]
    assert recovered[0]["event"]["status"] == "PROPOSED"
    assert "summary" not in json.dumps(recovered)
    assert result["executed"] is result["execution_authorized"] is False
    assert len(calls) == 1


def test_persistence_failure_blocks_release(tmp_path):
    boundary, request, calls, sink, _ = setup_boundary(tmp_path)
    sink.path.unlink()
    result = boundary.analyze(request)
    assert result["status"] == "NO_DECISION"
    assert result["reason"] == "audit_unavailable"
    assert result["audit_recorded"] is False
    assert "analysis" not in result
    assert not sink.path.exists()
    assert len(calls) == 1


def test_corruption_blocks_release(tmp_path):
    boundary, request, _, sink, _ = setup_boundary(tmp_path)
    with sqlite3.connect(sink.path) as db:
        db.execute("UPDATE head SET sequence=1")
    assert boundary.analyze(request)["status"] == "NO_DECISION"


class UnacknowledgedSink(DurableAuditSink):
    def __init__(self, receipt): self.receipt = receipt
    def append(self, event, *, idempotency_key): return self.receipt
    def history(self): return []


@pytest.mark.parametrize("receipt", [None, AuditReceipt("fake", 1, "digest"),
                                    AuditReceipt("fake", 1, "digest", durable=True)])
def test_absent_or_non_durable_receipt_blocks_release(tmp_path, receipt):
    boundary, request, _, _, _ = setup_boundary(tmp_path, sink=UnacknowledgedSink(receipt))
    result = boundary.analyze(request)
    assert result["status"] == "NO_DECISION"
    assert "analysis" not in result


def test_production_never_defaults_to_memory(monkeypatch):
    development = AuditTrail()
    monkeypatch.setenv("AEON_AUDIT_MODE", "production")
    for call in (lambda: AuditTrail(), lambda: AuditTrail(ImmutableAudit()),
                 lambda: AuditTrail(mode="development"), lambda: EvidenceGate({}),
                 lambda: EvidenceGate({}, audit=development)):
        with pytest.raises(AuditError):
            call()
    with pytest.raises(AuditError):
        GovernedAnalysis(router=ProviderRouter(), provider_name="fake",
                         evidence=None, capabilities={}, audit=development)


def test_collection_failures_are_durable_and_sanitized(tmp_path):
    _, _, _, sink, gate = setup_boundary(tmp_path)
    with pytest.raises(EvidenceError):
        gate.collect("fixture-secret-unknown-source")
    records = SQLiteAudit(sink.path).history()
    assert records[0]["event"]["event_type"] == "EVIDENCE_COLLECTION_FAILED"
    assert "fixture-secret" not in json.dumps(records)


def test_facade_idempotency_retry(tmp_path):
    _, _, _, sink, gate = setup_boundary(tmp_path)
    with pytest.raises(EvidenceError):
        gate.collect("unknown")
    event = sink.history()[0]["event"]
    audit = AuditTrail(sink, mode="production")
    first = audit.record(event, idempotency_key="stable-host-operation")
    second = audit.record(event, idempotency_key="stable-host-operation")
    assert first.audit_id == second.audit_id
    assert second.duplicate
    assert len(sink.history()) == 2


def test_explicit_production_rejects_development_evidence_gate(tmp_path):
    audit = AuditTrail(SQLiteAudit(tmp_path / "audit.db", create=True), mode="production")
    with pytest.raises(AuditError, match="durable_audit_required"):
        GovernedAnalysis(router=ProviderRouter(), provider_name="fake",
                         evidence=EvidenceGate({}), capabilities={},
                         audit=audit, audit_mode="production")


def test_existing_development_facade_cannot_silently_run_in_production(monkeypatch):
    audit = AuditTrail()
    monkeypatch.setenv("AEON_AUDIT_MODE", "production")
    with pytest.raises(AuditError, match="audit_mode_downgrade_denied"):
        audit.record({"event": "not persisted"})
    assert audit.report() == []
