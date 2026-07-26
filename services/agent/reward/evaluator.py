from dataclasses import dataclass


@dataclass
class RewardSignal:
    agent_id: str
    task: str
    score: float
    metadata: dict


class RewardEvaluator:

    def evaluate(self, agent_id: str, task: str, success: bool):
        score = 1.0 if success else 0.0

        return RewardSignal(
            agent_id=agent_id,
            task=task,
            score=score,
            metadata={"evaluated": True}
        )
