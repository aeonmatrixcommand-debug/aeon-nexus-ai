from __future__ import annotations

import json
from datetime import datetime, timezone

from providers.bailian.audit import (
    build_audit_record,
    serialize_audit_record,
)
from providers.bailian.guardian import BailianGuardianGate
from providers.bailian.models import BailianHealthSnapshot


def make_snapshot() -> BailianHealthSnapshot:
    return BailianHealthSnapshot(
        provider="alibaba-bailian",
        model="qwen3.8-max",
        endpoint="https://dashscope-intl.aliyuncs.com/api/v1",
        runtime_call="success",
        exit_code=0,
        latency_ms=3710,
        captured_at=datetime(
            2026,
            9,
            13,
            20,
            41,
            30,
            tzinfo=timezone.utc,
        ),
        evidence_status="OBSERVED",
    )


def test_audit_record_contains_guardian_decision() -> None:
    snapshot = make_snapshot()
    guardian = BailianGuardianGate().evaluate_health(snapshot)

    record = build_audit_record(snapshot, guardian)

    assert record.event_type == "BAILIAN_RUNTIME_HEALTH"
    assert record.guardian_decision == "ALLOW"
    assert record.guardian_reason == "OBSERVED_RUNTIME_SUCCESS"


def test_evidence_hash_is_deterministic() -> None:
    snapshot = make_snapshot()
    guardian = BailianGuardianGate().evaluate_health(snapshot)

    first = build_audit_record(snapshot, guardian)
    second = build_audit_record(snapshot, guardian)

    assert first.evidence_hash == second.evidence_hash
    assert len(first.evidence_hash) == 64


def test_audit_serialization_is_valid_json() -> None:
    snapshot = make_snapshot()
    guardian = BailianGuardianGate().evaluate_health(snapshot)

    record = build_audit_record(snapshot, guardian)
    serialized = serialize_audit_record(record)

    payload = json.loads(serialized)

    assert payload["provider"] == "alibaba-bailian"
    assert payload["guardian_decision"] == "ALLOW"
    assert payload["evidence_hash"] == record.evidence_hash
