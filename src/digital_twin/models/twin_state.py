from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Any


@dataclass
class DigitalTwinState:
    """
    Shared Reality Model between Human and AI.
    """

    entity_id: str
    entity_type: str

    current_state: Dict[str, Any] = field(default_factory=dict)

    risks: List[Dict[str, Any]] = field(default_factory=list)

    causes: List[str] = field(default_factory=list)

    impacts: Dict[str, Any] = field(default_factory=dict)

    recommendations: List[str] = field(default_factory=list)

    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def add_risk(
        self,
        risk_type: str,
        severity: str,
        probability: float
    ):
        self.risks.append(
            {
                "type": risk_type,
                "severity": severity,
                "probability": probability
            }
        )

    def add_recommendation(self, action: str):
        self.recommendations.append(action)
