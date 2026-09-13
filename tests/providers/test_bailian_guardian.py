from __future__ import annotations

from datetime import datetime, timezone

from providers.bailian.guardian import BailianGuardianGate
from providers.bailian.models import BailianHealthSnapshot


def make_snapshot(
    *,
    runtime_call="success",
    exit_code=0,
    latency_ms=100,
    evidence_status="OBSERVED",
):
    return BailianHealthSnapshot(
        provider="alibaba-bailian",
        model="qwen3.8-max",
        endpoint="https://dashscope-intl.aliyuncs.com/api/v1",
        runtime_call=runtime_call,
        exit_code=exit_code,
        latency_ms=latency_ms,
        captured_at=datetime.now(timezone.utc),
        evidence_status=evidence_status,
    )


def test_guardian_allows_observed_success() -> None:
    result = BailianGuardianGate().evaluate_health(make_snapshot())

    assert result.decision == "ALLOW"
    assert result.reason == "OBSERVED_RUNTIME_SUCCESS"


def test_guardian_denies_failed_runtime() -> None:
    result = BailianGuardianGate().evaluate_health(
        make_snapshot(runtime_call="failed")
    )

    assert result.decision == "DENY"
    assert result.reason == "RUNTIME_FAILED"


def test_guardian_denies_nonzero_exit() -> None:
    result = BailianGuardianGate().evaluate_health(
        make_snapshot(exit_code=1)
    )

    assert result.decision == "DENY"
    assert result.reason == "NONZERO_EXIT_CODE"


def test_guardian_denies_missing_latency() -> None:
    result = BailianGuardianGate().evaluate_health(
        make_snapshot(latency_ms=None)
    )

    assert result.decision == "DENY"
    assert result.reason == "MISSING_LATENCY"


def test_guardian_denies_insufficient_evidence() -> None:
    result = BailianGuardianGate().evaluate_health(
        make_snapshot(evidence_status="INSUFFICIENT_EVIDENCE")
    )

    assert result.decision == "DENY"
    assert result.reason == "INSUFFICIENT_EVIDENCE"
