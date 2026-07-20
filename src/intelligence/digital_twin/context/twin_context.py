"""
AEON MATRIX Twin Context Injection Layer
Sprint 79.9
"""

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class TwinContext:
    entity_type: str
    entity_id: str
    operational_state: str
    confidence: float
    simulation_result: dict
    timestamp: str


class TwinContextAdapter:
    """
    Converts Digital Twin state into
    Mother Brain reasoning context.
    """

    def inject(
        self,
        entity_type: str,
        entity_id: str,
        operational_state: str,
        confidence: float,
        simulation_result: dict,
    ) -> TwinContext:

        return TwinContext(
            entity_type=entity_type,
            entity_id=entity_id,
            operational_state=operational_state,
            confidence=confidence,
            simulation_result=simulation_result,
            timestamp=datetime.now(UTC).isoformat(),
        )
