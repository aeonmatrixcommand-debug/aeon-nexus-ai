"""Governance-only authorization gate for promotion proposals."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from src.intelligence.ecdt.promotion_authorization import (
    PromotionAuthorization,
)


class PromotionAuthorizationGate:
    """Evaluate whether an approved proposal may be authorized.

    This component creates authorization artifacts only.
    Authorization never implies application or execution.
    """

    def evaluate(
        self,
        proposal: Dict[str, Any],
        *,
        authorized_by: str | None = None,
        policy: Dict[str, Any] | None = None,
        scope: Dict[str, Any] | None = None,
        constraints: Dict[str, Any] | None = None,
        expires_at: str | None = None,
    ) -> PromotionAuthorization:
        proposal_snapshot = deepcopy(proposal)
        effective_policy = deepcopy(policy or {})
        effective_scope = deepcopy(scope or {})
        effective_constraints = deepcopy(constraints or {})

        proposal_status = proposal_snapshot.get("status")

        if proposal_status != "PROPOSED":
            status = "REJECTED"
            reason = "proposal_not_proposed"
        elif not authorized_by:
            status = "HUMAN_REQUIRED"
            reason = "explicit_authorizer_required"
        elif effective_policy.get("allowed") is False:
            status = "REJECTED"
            reason = "policy_denied"
        else:
            status = "AUTHORIZED"
            reason = "governance_authorized"

        return PromotionAuthorization(
            proposal_id=proposal_snapshot.get(
                "proposal_id",
                "",
            ),
            candidate_id=proposal_snapshot.get(
                "candidate_id",
                "",
            ),
            decision_id=proposal_snapshot.get(
                "decision_id",
                "",
            ),
            correlation_id=proposal_snapshot.get(
                "correlation_id",
                "",
            ),
            status=status,
            authorized_by=authorized_by or "",
            policy=effective_policy,
            scope=effective_scope,
            constraints=effective_constraints,
            expires_at=expires_at,
            reason=reason,
        )
