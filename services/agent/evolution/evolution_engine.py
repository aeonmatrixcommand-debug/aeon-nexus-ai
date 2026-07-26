from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class EvolutionSignal:
    agent_id: str
    outcome: str
    score: float
    created_at: datetime


class AgentEvolutionEngine:
    def __init__(self):
        self.signals = []

    def evaluate(self, agent_id: str, outcome: str, score: float):
        signal = EvolutionSignal(
            agent_id=agent_id,
            outcome=outcome,
            score=score,
            created_at=datetime.now(UTC),
        )

        self.signals.append(signal)

        return signal
