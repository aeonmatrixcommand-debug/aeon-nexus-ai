"""Governance gate for ECDT learning candidates.

The gate classifies candidates only. Approval is not
authorization to execute, deploy, mutate, or promote anything.
"""

from __future__ import annotations

from typing import Any, Dict

from src.intelligence.ecdt.learning_approval import (
    LearningApproval,
    LearningApprovalStatus,
)


class LearningApprovalGate:
    """Classify a learning candidate through explicit governance."""

    def evaluate(
        self,
        candidate: Dict[str, Any],
        *,
        human_approved: bool = False,
    ) -> LearningApproval:
        snapshot = dict(candidate)

        candidate_id = snapshot.get("candidate_id")
        if not candidate_id:
            raise ValueError("candidate_id is required")

        eligible = bool(snapshot.get("eligible", False))
        requires_human = bool(
            snapshot.get("human_review_required", False)
        )

        if not eligible:
            return LearningApproval(
                candidate_id=candidate_id,
                status=LearningApprovalStatus.REJECTED,
                reason="candidate_not_eligible",
                evidence=snapshot,
            )

        if requires_human and not human_approved:
            return LearningApproval(
                candidate_id=candidate_id,
                status=(
                    LearningApprovalStatus.HUMAN_REVIEW_REQUIRED
                ),
                reason="explicit_human_approval_required",
                evidence=snapshot,
            )

        return LearningApproval(
            candidate_id=candidate_id,
            status=LearningApprovalStatus.APPROVED,
            reason=(
                "human_approved"
                if requires_human
                else "governance_criteria_satisfied"
            ),
            evidence=snapshot,
        )
