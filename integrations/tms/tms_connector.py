"""Read-only, governance-gated adapter for TMS route analysis."""

from dataclasses import dataclass
from numbers import Real
from typing import Any, Mapping

from services.agents.governance.agent_governance import (
    AgentGovernanceEngine,
)
from services.guardian.tms_intelligence.runtime import TMSIntelligence


READ_ROUTE_CAPABILITY = "tms.route.analyze.read"


@dataclass(frozen=True)
class _ConnectorIdentity:
    name: str = "adk_tms_readonly_connector"
    capabilities: frozenset[str] = frozenset({READ_ROUTE_CAPABILITY})


class TMSReadOnlyConnector:
    """Expose TMS route analysis without transactional operations."""

    def __init__(
        self,
        intelligence: TMSIntelligence | None = None,
        governance: AgentGovernanceEngine | None = None,
    ):
        self._intelligence = intelligence or TMSIntelligence()
        self._governance = governance or AgentGovernanceEngine()
        self._identity = _ConnectorIdentity()

    def analyze_route(
        self,
        route: Mapping[str, Any],
    ) -> dict[str, Any]:
        task = {
            "capability": READ_ROUTE_CAPABILITY,
            "critical": False,
            "operation": "analyze_route",
            "mode": "READ_ONLY",
        }
        decision = self._governance.authorize_execution(
            self._identity,
            task,
        )
        audit = dict(self._governance.audit_log[-1])

        if decision != "ALLOW":
            return {
                "status": "BLOCKED",
                "mode": "READ_ONLY",
                "executed": False,
                "reason": "governance_denied",
                "audit": audit,
            }

        if not isinstance(route, Mapping):
            return self._no_decision(
                "route_mapping_required",
                audit,
            )

        distance = route.get("distance")
        if (
            isinstance(distance, bool)
            or not isinstance(distance, Real)
            or distance <= 0
        ):
            return self._no_decision(
                "positive_numeric_distance_required",
                audit,
            )

        result = self._intelligence.analyze_route(
            {"distance": float(distance)}
        )
        return {
            "status": "OK",
            "mode": "READ_ONLY",
            "executed": True,
            "result": result,
            "audit": audit,
        }

    @staticmethod
    def _no_decision(
        reason: str,
        audit: dict[str, Any],
    ) -> dict[str, Any]:
        return {
            "status": "NO_DECISION",
            "mode": "READ_ONLY",
            "executed": False,
            "axiom": "No Evidence -> No Decision",
            "reason": reason,
            "audit": audit,
        }
