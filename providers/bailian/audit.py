from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

from .guardian import BailianGuardianResult
from .models import BailianHealthSnapshot


@dataclass(frozen=True)
class BailianAuditRecord:
    event_type: str
    captured_at: str
    provider: str
    model: str
    endpoint: str
    runtime_call: str
    exit_code: int | None
    latency_ms: int | None
    evidence_status: str
    guardian_decision: str
    guardian_reason: str
    evidence_hash: str


def _canonical_json(payload: dict[str, Any]) -> str:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def _hash_snapshot(snapshot: BailianHealthSnapshot) -> str:
    payload = {
        "provider": snapshot.provider,
        "model": snapshot.model,
        "endpoint": snapshot.endpoint,
        "runtime_call": snapshot.runtime_call,
        "exit_code": snapshot.exit_code,
        "latency_ms": snapshot.latency_ms,
        "captured_at": snapshot.captured_at.isoformat(),
        "evidence_status": snapshot.evidence_status,
    }

    canonical = _canonical_json(payload)

    return hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()


def build_audit_record(
    snapshot: BailianHealthSnapshot,
    guardian: BailianGuardianResult,
) -> BailianAuditRecord:
    return BailianAuditRecord(
        event_type="BAILIAN_RUNTIME_HEALTH",
        captured_at=datetime.now(timezone.utc).isoformat(),
        provider=snapshot.provider,
        model=snapshot.model,
        endpoint=snapshot.endpoint,
        runtime_call=snapshot.runtime_call,
        exit_code=snapshot.exit_code,
        latency_ms=snapshot.latency_ms,
        evidence_status=snapshot.evidence_status,
        guardian_decision=guardian.decision,
        guardian_reason=guardian.reason,
        evidence_hash=_hash_snapshot(snapshot),
    )


def serialize_audit_record(record: BailianAuditRecord) -> str:
    return _canonical_json(asdict(record))
