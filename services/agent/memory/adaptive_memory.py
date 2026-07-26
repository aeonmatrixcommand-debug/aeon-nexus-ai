from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Experience:
    task: str
    action: str
    outcome: str
    score: float
    timestamp: datetime = field(default_factory=datetime.utcnow)


class AdaptiveMemory:
    """
    Agent experience memory for autonomous learning.
    """

    def __init__(self):
        self.experiences: list[Experience] = []

    def remember(
        self,
        task: str,
        action: str,
        outcome: str,
        score: float,
    ):
        self.experiences.append(
            Experience(
                task=task,
                action=action,
                outcome=outcome,
                score=score,
            )
        )

    def recall(self):
        return self.experiences
