"""Immutable proposal describing an intended governed change.

A PromotionProposal is evidence for a future governance step.
It cannot apply, deploy, execute, or mutate production state.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4


def _identifier() -> str:
    return f"promotion-proposal-{uuid4()}"


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class PromotionProposal:
    candidate_id: str
    approval_id: str
    correlation_id: str
    intended_change: Dict[str, Any]
    evidence: Dict[str, Any] = field(default_factory=dict)
    risk: Dict[str, Any] = field(default_factory=dict)
    proposal_id: str = field(default_factory=_identifier)
    timestamp: str = field(default_factory=_timestamp)
    status: str = "PROPOSED"

    def to_dict(self) -> Dict[str, Any]:
        """Return a defensive representation of the proposal."""
        return deepcopy(
            {
                "proposal_id": self.proposal_id,
                "candidate_id": self.candidate_id,
                "approval_id": self.approval_id,
                "correlation_id": self.correlation_id,
                "intended_change": self.intended_change,
                "evidence": self.evidence,
                "risk": self.risk,
                "timestamp": self.timestamp,
                "status": self.status,
            }
        )
