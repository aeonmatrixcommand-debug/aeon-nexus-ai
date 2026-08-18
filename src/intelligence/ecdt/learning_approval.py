"""Governed approval result for an ECDT learning candidate.

This object records a governance decision only.
It has no authority to execute, deploy, mutate policy,
modify models, or promote production behavior.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict
from uuid import uuid4


class LearningApprovalStatus(str, Enum):
    REJECTED = "REJECTED"
    HUMAN_REVIEW_REQUIRED = "HUMAN_REVIEW_REQUIRED"
    APPROVED = "APPROVED"


def _identifier(prefix: str) -> str:
    return f"{prefix}-{uuid4()}"


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class LearningApproval:
    candidate_id: str
    status: LearningApprovalStatus
    reason: str
    approval_id: str = field(
        default_factory=lambda: _identifier("approval")
    )
    timestamp: str = field(default_factory=_timestamp)
    evidence: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return deepcopy(
            {
                "approval_id": self.approval_id,
                "candidate_id": self.candidate_id,
                "status": self.status.value,
                "reason": self.reason,
                "timestamp": self.timestamp,
                "evidence": self.evidence,
            }
        )
