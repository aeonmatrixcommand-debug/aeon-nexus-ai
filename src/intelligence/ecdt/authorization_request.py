from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping


@dataclass(frozen=True)
class AuthorizationRequest:
    """Request for authorization. This object grants no authority."""

    request_id: str
    proposal_id: str
    status: str
    intended_change: Mapping[str, Any]
    evidence: Mapping[str, Any]
    trace: tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "request_id": self.request_id,
            "proposal_id": self.proposal_id,
            "status": self.status,
            "intended_change": dict(self.intended_change),
            "evidence": dict(self.evidence),
            "trace": list(self.trace),
        }
