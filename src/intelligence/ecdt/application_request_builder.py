"""Builder for controlled ECDT application requests."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from .application_request import ApplicationRequest


class ApplicationRequestBuilder:
    """Build an application request without applying any change."""

    def build(
        self,
        *,
        proposal: Dict[str, Any],
        authorization: Dict[str, Any],
    ) -> ApplicationRequest:
        proposal_data = deepcopy(proposal)
        authorization_data = deepcopy(authorization)

        if authorization_data.get("status") != "AUTHORIZED":
            raise ValueError("authorization must be AUTHORIZED")

        proposal_id = proposal_data.get("proposal_id")
        authorization_proposal_id = authorization_data.get(
            "proposal_id"
        )

        if not proposal_id:
            raise ValueError("proposal_id is required")

        if authorization_proposal_id != proposal_id:
            raise ValueError(
                "authorization does not match proposal"
            )

        authorization_id = authorization_data.get(
            "authorization_id"
        )
        if not authorization_id:
            raise ValueError("authorization_id is required")

        correlation_id = proposal_data.get("correlation_id")
        if not correlation_id:
            raise ValueError("correlation_id is required")

        intended_change = proposal_data.get("intended_change")
        if not isinstance(intended_change, dict):
            raise ValueError("intended_change is required")

        return ApplicationRequest(
            proposal_id=proposal_id,
            authorization_id=authorization_id,
            correlation_id=correlation_id,
            intended_change=intended_change,
        )
