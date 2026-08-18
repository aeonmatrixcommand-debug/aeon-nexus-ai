"""Governed promotion authorization artifact.

Authorization represents permission granted by governance.
It does not apply, deploy, execute, or promote a change.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4


@dataclass(frozen=True)
class PromotionAuthorization:
    """Immutable authorization artifact for a promotion proposal."""

    proposal_id: str
    candidate_id: str
    decision_id: str
    correlation_id: str
    status: str
    authorized_by: str
    policy: Dict[str, Any] = field(default_factory=dict)
    scope: Dict[str, Any] = field(default_factory=dict)
    constraints: Dict[str, Any] = field(default_factory=dict)
    expires_at: str | None = None
    reason: str = ""
    authorization_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    created_at: str = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        ).isoformat()
    )

    def to_dict(self) -> Dict[str, Any]:
        """Return a defensive representation of the artifact."""
        return deepcopy(
            {
                "authorization_id": self.authorization_id,
                "proposal_id": self.proposal_id,
                "candidate_id": self.candidate_id,
                "decision_id": self.decision_id,
                "correlation_id": self.correlation_id,
                "status": self.status,
                "authorized_by": self.authorized_by,
                "policy": self.policy,
                "scope": self.scope,
                "constraints": self.constraints,
                "expires_at": self.expires_at,
                "reason": self.reason,
                "created_at": self.created_at,
            }
        )
