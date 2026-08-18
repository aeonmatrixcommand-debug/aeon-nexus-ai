"""Governed learning candidate for ECDT.

A learning candidate is advisory only.

It may describe a possible future adjustment, but it cannot
execute actions, modify policy, mutate decision memory, or
activate autonomous learning.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4


def _candidate_id() -> str:
    return f"lc-{uuid4()}"


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class LearningCandidate:
    """Immutable proposal for governed organizational learning."""

    source_decision_id: str
    correlation_id: str

    candidate_id: str = field(default_factory=_candidate_id)
    timestamp: str = field(default_factory=_timestamp)

    evidence: Dict[str, Any] = field(default_factory=dict)
    observed_delta: Dict[str, Any] = field(default_factory=dict)
    proposed_adjustment: Dict[str, Any] = field(default_factory=dict)

    confidence: float = 0.0
    requires_review: bool = True

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")

        if self.requires_review is not True:
            raise ValueError(
                "learning candidates must require governance review"
            )

        object.__setattr__(self, "evidence", deepcopy(self.evidence))
        object.__setattr__(
            self,
            "observed_delta",
            deepcopy(self.observed_delta),
        )
        object.__setattr__(
            self,
            "proposed_adjustment",
            deepcopy(self.proposed_adjustment),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Return a defensive representation of the candidate."""

        return deepcopy(
            {
                "candidate_id": self.candidate_id,
                "source_decision_id": self.source_decision_id,
                "correlation_id": self.correlation_id,
                "timestamp": self.timestamp,
                "evidence": self.evidence,
                "observed_delta": self.observed_delta,
                "proposed_adjustment": self.proposed_adjustment,
                "confidence": self.confidence,
                "requires_review": self.requires_review,
            }
        )
