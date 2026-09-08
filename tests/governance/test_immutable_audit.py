"""Mutation isolation only; production durability is NOT ESTABLISHED."""

from concurrent.futures import ThreadPoolExecutor

import pytest

from ai_gateway.audit import AuditTrail
from src.governance.immutable_audit import ImmutableAudit


def test_nested_mutation_isolation():
    sink = ImmutableAudit()
    event = {"nested": {"items": [{"value": 1}]}}
    receipt = sink.append(event)
    event["nested"]["items"][0]["value"] = 2
    history = sink.history()
    history[0]["event"]["nested"]["items"].append(3)
    history.clear()
    assert sink.history()[0]["event"] == {"nested": {"items": [{"value": 1}]}}
    with pytest.raises(AttributeError):
        receipt.audit_id = "changed"


def test_facade_does_not_expose_live_storage():
    audit = AuditTrail()
    audit.record({"nested": [1]})
    audit.logs[0]["event"]["nested"].append(2)
    assert audit.report()[0]["event"] == {"nested": [1]}


def test_process_local_only():
    first = ImmutableAudit()
    first.append({"event": "recorded"})
    assert ImmutableAudit().history() == []


def test_concurrent_append_preserves_process_local_records():
    sink = ImmutableAudit()
    with ThreadPoolExecutor(max_workers=4) as pool:
        receipts = list(pool.map(lambda n: sink.append({"n": n}), range(20)))
    assert {r.sequence for r in receipts} == set(range(1, 21))
    assert len({r.audit_id for r in receipts}) == 20
    assert {r["event"]["n"] for r in sink.history()} == set(range(20))


def test_invalid_snapshot_is_not_appended():
    sink = ImmutableAudit()
    with pytest.raises(ValueError):
        sink.append({"value": float("nan")})
    assert sink.history() == []
