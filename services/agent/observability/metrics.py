from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class LearningMetric:
    agent_id: str
    metric: str
    value: float
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


class LearningMetricsStore:
    def __init__(self):
        self.metrics = []

    def record(self, metric: LearningMetric):
        self.metrics.append(metric)

    def latest(self):
        return self.metrics[-1] if self.metrics else None
