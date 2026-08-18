"""Controlled application request artifact for ECDT.

An ApplicationRequest represents an authorized request for a
future change. It does not apply, execute, deploy, or promote
anything.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4


@dataclass(frozen=True)
class ApplicationRequest:
    """Immutable description of an authorized application request."""

    proposal_id: str
    authorization_id: str
    correlation_id: str
    intended_change: Dict[str, Any]

    application_request_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    status: str = "REQUESTED"
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def __post_init__(self) -> None:
        if not self.proposal_id:
            raise ValueError("proposal_id is required")

        if not self.authorization_id:
            raise ValueError("authorization_id is required")

        if not self.correlation_id:
            raise ValueError("correlation_id is required")

        if not isinstance(self.intended_change, dict):
            raise TypeError("intended_change must be a dict")

        object.__setattr__(
            self,
            "intended_change",
            deepcopy(self.intended_change),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Return a defensive representation of this request."""
        return {
            "application_request_id": self.application_request_id,
            "proposal_id": self.proposal_id,
            "authorization_id": self.authorization_id,
            "correlation_id": self.correlation_id,
            "intended_change": deepcopy(self.intended_change),
            "status": self.status,
            "created_at": self.created_at,
        }
