"""Build governed learning candidates from evaluated outcomes."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from src.intelligence.ecdt.learning_candidate import LearningCandidate


class LearningCandidateBuilder:
    """Translate evaluation evidence into a review-only candidate."""

    def build(
        self,
        *,
        source_decision_id: str,
        correlation_id: str,
        evaluation: Dict[str, Any],
        proposed_adjustment: Dict[str, Any],
        confidence: float,
    ) -> LearningCandidate:
        """Build a candidate without executing or mutating anything."""

        if not source_decision_id:
            raise ValueError("source_decision_id is required")

        if not correlation_id:
            raise ValueError("correlation_id is required")

        if not isinstance(evaluation, dict):
            raise TypeError("evaluation must be a dict")

        if not isinstance(proposed_adjustment, dict):
            raise TypeError("proposed_adjustment must be a dict")

        evaluation_snapshot = deepcopy(evaluation)

        observed_delta = deepcopy(
            evaluation_snapshot.get(
                "delta",
                evaluation_snapshot.get("differences", {}),
            )
        )

        return LearningCandidate(
            source_decision_id=source_decision_id,
            correlation_id=correlation_id,
            evidence=evaluation_snapshot,
            observed_delta=observed_delta,
            proposed_adjustment=deepcopy(proposed_adjustment),
            confidence=confidence,
            requires_review=True,
        )
