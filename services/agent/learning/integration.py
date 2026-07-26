from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class AgentLearningState:
    agent_id: str
    memory_score: float
    collaboration_score: float
    reward_score: float
    evolution_score: float
    updated_at: datetime = datetime.now(UTC)


class AgentLearningIntegrator:

    def integrate(
        self,
        agent_id: str,
        memory_score: float,
        collaboration_score: float,
        reward_score: float,
        evolution_score: float,
    ) -> AgentLearningState:

        return AgentLearningState(
            agent_id=agent_id,
            memory_score=memory_score,
            collaboration_score=collaboration_score,
            reward_score=reward_score,
            evolution_score=evolution_score,
        )
