from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class LearningEvent:
    agent_id: str
    event_type: str
    payload: dict
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


class LearningEventBus:
    def __init__(self):
        self.events = []

    def publish(self, event: LearningEvent):
        self.events.append(event)

    def latest(self):
        return self.events[-1] if self.events else None
