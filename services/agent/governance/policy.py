from dataclasses import dataclass


@dataclass
class LearningPolicy:
    reward_threshold: float = 0.8
    allow_evolution: bool = True


class LearningPolicyEngine:
    def __init__(self, policy: LearningPolicy | None = None):
        self.policy = policy or LearningPolicy()

    def evaluate(self, reward: float) -> bool:
        if not self.policy.allow_evolution:
            return False

        return reward >= self.policy.reward_threshold
