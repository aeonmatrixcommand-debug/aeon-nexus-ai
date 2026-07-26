from dataclasses import dataclass


@dataclass
class AgentContract:
    agent_id: str
    capability: str
    trust_score: float = 1.0
