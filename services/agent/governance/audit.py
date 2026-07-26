from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class LearningAuditRecord:
    agent_id: str
    event: str
    previous_score: float
    new_score: float
    reason: str
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


class LearningAuditTrail:
    def __init__(self):
        self.records = []

    def record(self, audit: LearningAuditRecord):
        self.records.append(audit)

    def latest(self):
        return self.records[-1] if self.records else None
