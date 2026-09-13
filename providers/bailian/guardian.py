from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .models import BailianHealthSnapshot


GuardianDecision = Literal["ALLOW", "DENY"]


@dataclass(frozen=True)
class BailianGuardianResult:
    decision: GuardianDecision
    reason: str


class BailianGuardianGate:
    def evaluate_health(
        self,
        snapshot: BailianHealthSnapshot,
    ) -> BailianGuardianResult:
        if snapshot.evidence_status != "OBSERVED":
            return BailianGuardianResult(
                decision="DENY",
                reason="INSUFFICIENT_EVIDENCE",
            )

        if snapshot.runtime_call != "success":
            return BailianGuardianResult(
                decision="DENY",
                reason="RUNTIME_FAILED",
            )

        if snapshot.exit_code != 0:
            return BailianGuardianResult(
                decision="DENY",
                reason="NONZERO_EXIT_CODE",
            )

        if snapshot.latency_ms is None:
            return BailianGuardianResult(
                decision="DENY",
                reason="MISSING_LATENCY",
            )

        return BailianGuardianResult(
            decision="ALLOW",
            reason="OBSERVED_RUNTIME_SUCCESS",
        )
