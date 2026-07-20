from dataclasses import dataclass


@dataclass
class AgentProfile:
    name: str
    capability: str
    confidence: float
    cost: float
    sla: str
