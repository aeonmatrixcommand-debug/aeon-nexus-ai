from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping

from .authorization_request import AuthorizationRequest


class AuthorizationRequestBuilder:
    """Build authorization requests without granting authorization."""

    def build(
        self,
        *,
        proposal: Any,
    ) -> AuthorizationRequest:
        data = self._as_mapping(proposal)

        proposal_id = str(data.get("proposal_id", "")).strip()
        if not proposal_id:
            raise ValueError("proposal_id is required")

        if data.get("status") != "PROPOSED":
            raise ValueError("proposal must have PROPOSED status")

        action = str(data.get("action", "")).strip()
        if not action:
            raise ValueError("proposal action is required")

        evidence = data.get("evidence")
        if not isinstance(evidence, Mapping) or not evidence:
            raise ValueError("proposal evidence is required")

        intended_change = {
            "action": action,
        }

        canonical = json.dumps(
            {
                "proposal_id": proposal_id,
                "intended_change": intended_change,
            },
            sort_keys=True,
            separators=(",", ":"),
        )

        request_id = (
            "authreq-"
            + hashlib.sha256(canonical.encode()).hexdigest()[:16]
        )

        trace = (
            f"request_id={request_id}",
            f"proposal_id={proposal_id}",
            "status=REQUESTED",
            "authorization_granted=false",
        )

        return AuthorizationRequest(
            request_id=request_id,
            proposal_id=proposal_id,
            status="REQUESTED",
            intended_change=intended_change,
            evidence=dict(evidence),
            trace=trace,
        )

    @staticmethod
    def _as_mapping(value: Any) -> Mapping[str, Any]:
        if isinstance(value, Mapping):
            return value

        to_dict = getattr(value, "to_dict", None)
        if callable(to_dict):
            result = to_dict()
            if isinstance(result, Mapping):
                return result

        raise TypeError("proposal must be mapping-compatible")
