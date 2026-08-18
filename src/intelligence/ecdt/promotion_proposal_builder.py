"""Governed builder for ECDT promotion proposals.

Only an explicitly APPROVED learning approval can produce a
proposal. Producing a proposal grants no production authority.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from src.intelligence.ecdt.promotion_proposal import (
    PromotionProposal,
)


class PromotionProposalBuilder:
    """Build inert promotion proposals from approved artifacts."""

    def build(
        self,
        *,
        candidate: Dict[str, Any],
        approval: Dict[str, Any],
        intended_change: Dict[str, Any],
        risk: Dict[str, Any] | None = None,
    ) -> PromotionProposal:
        candidate_snapshot = deepcopy(candidate)
        approval_snapshot = deepcopy(approval)

        candidate_id = candidate_snapshot.get("candidate_id")
        if not candidate_id:
            raise ValueError("candidate_id is required")

        approval_id = approval_snapshot.get("approval_id")
        if not approval_id:
            raise ValueError("approval_id is required")

        if approval_snapshot.get("status") != "APPROVED":
            raise ValueError(
                "promotion proposal requires APPROVED learning approval"
            )

        approved_candidate_id = approval_snapshot.get("candidate_id")
        if approved_candidate_id != candidate_id:
            raise ValueError(
                "approval candidate_id does not match candidate"
            )

        correlation_id = candidate_snapshot.get("correlation_id")
        if not correlation_id:
            raise ValueError("correlation_id is required")

        if not intended_change:
            raise ValueError("intended_change is required")

        return PromotionProposal(
            candidate_id=candidate_id,
            approval_id=approval_id,
            correlation_id=correlation_id,
            intended_change=deepcopy(intended_change),
            evidence={
                "candidate": candidate_snapshot,
                "approval": approval_snapshot,
            },
            risk=deepcopy(risk or {}),
        )
