from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class LearningTrace:
    agent_id: str
    action: str
    outcome: str
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


class LearningTracer:
    def __init__(self):
        self.traces = []

    def trace(self, item: LearningTrace):
        self.traces.append(item)

    def last(self):
        return self.traces[-1] if self.traces else None
