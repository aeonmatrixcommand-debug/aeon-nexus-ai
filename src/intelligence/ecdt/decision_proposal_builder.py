"""Build governed ECDT decision proposals from recommendations."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping

from .decision_proposal import DecisionProposal


class DecisionProposalBuilder:
    """Create deterministic proposals without granting authority."""

    def build(
        self,
        *,
        recommendation: Mapping[str, Any],
        evidence: Mapping[str, Any],
        policy_context: Mapping[str, Any] | None = None,
    ) -> DecisionProposal:
        if not isinstance(recommendation, Mapping):
            raise TypeError("recommendation must be mapping-compatible")

        scenario_name = str(
            recommendation.get("name", "")
        ).strip()
        if not scenario_name:
            raise ValueError("recommendation name is required")

        action = str(
            recommendation.get("action", "")
        ).strip()
        if not action:
            raise ValueError("recommendation action is required")

        if not isinstance(evidence, Mapping) or not evidence:
            raise ValueError("evidence is required")

        policy = dict(policy_context or {})

        proposal_id = self._proposal_id(
            scenario_name=scenario_name,
            action=action,
            evidence=evidence,
            policy_context=policy,
        )

        trace = (
            f"scenario={scenario_name}",
            f"action={action}",
            f"proposal_id={proposal_id}",
            "status=PROPOSED",
            "execution_authorized=false",
        )

        return DecisionProposal(
            proposal_id=proposal_id,
            status="PROPOSED",
            scenario_name=scenario_name,
            action=action,
            evidence=dict(evidence),
            policy_context=policy,
            trace=trace,
        )

    @staticmethod
    def _proposal_id(
        *,
        scenario_name: str,
        action: str,
        evidence: Mapping[str, Any],
        policy_context: Mapping[str, Any],
    ) -> str:
        payload = {
            "scenario_name": scenario_name,
            "action": action,
            "evidence": evidence,
            "policy_context": policy_context,
        }

        canonical = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        )

        digest = hashlib.sha256(
            canonical.encode("utf-8")
        ).hexdigest()[:16]

        return f"proposal-{digest}"
