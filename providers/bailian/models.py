from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Literal


EvidenceStatus = Literal["OBSERVED", "PARTIAL", "INSUFFICIENT_EVIDENCE"]


@dataclass(frozen=True)
class BailianHealthSnapshot:
    provider: str
    model: str
    endpoint: str
    runtime_call: Literal["success", "failed"]
    exit_code: int | None
    latency_ms: int | None
    captured_at: datetime
    evidence_status: EvidenceStatus
    stdout: str | None = None
    stderr: str | None = None
