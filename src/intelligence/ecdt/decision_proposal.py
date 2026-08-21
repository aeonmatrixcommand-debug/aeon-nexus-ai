"""Immutable ECDT decision proposal model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping, Tuple


@dataclass(frozen=True)
class DecisionProposal:
    proposal_id: str
    status: str
    scenario_name: str
    action: str
    evidence: Mapping[str, Any]
    policy_context: Mapping[str, Any]
    trace: Tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "proposal_id": self.proposal_id,
            "status": self.status,
            "scenario_name": self.scenario_name,
            "action": self.action,
            "evidence": dict(self.evidence),
            "policy_context": dict(self.policy_context),
            "trace": list(self.trace),
        }
