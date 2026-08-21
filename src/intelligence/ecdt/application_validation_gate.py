from __future__ import annotations

from typing import Any, Mapping

from .application_validation import ApplicationValidation


class ApplicationValidationGate:
    """Validation-only gate. VALIDATED does not mean APPLIED."""

    def evaluate(
        self,
        request: Any,
        *,
        policy: Mapping[str, Any] | None = None,
    ) -> ApplicationValidation:
        if request is None:
            raise ValueError("request is required")

        data = self._as_mapping(request)

        request_id = str(data.get("request_id", "")).strip()
        if not request_id:
            raise ValueError("request_id is required")

        reasons: list[str] = []

        if data.get("status") != "REQUESTED":
            reasons.append("REQUEST_NOT_REQUESTED")

        if not str(data.get("authorization_id", "")).strip():
            reasons.append("AUTHORIZATION_LINK_REQUIRED")

        if not str(data.get("proposal_id", "")).strip():
            reasons.append("PROPOSAL_LINK_REQUIRED")

        intended_change = data.get("intended_change")
        if not isinstance(intended_change, Mapping) or not intended_change:
            reasons.append("INTENDED_CHANGE_REQUIRED")

        if policy is not None and policy.get("allowed") is not True:
            reasons.append("POLICY_NOT_ALLOWED")

        return ApplicationValidation(
            request_id=request_id,
            status="REJECTED" if reasons else "VALIDATED",
            reasons=tuple(reasons),
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

        raise TypeError("request must be mapping-compatible")
