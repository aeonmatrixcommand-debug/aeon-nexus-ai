from dataclasses import dataclass, asdict
from datetime import datetime
import uuid


@dataclass
class OutcomeEvent:

    trace_id: str
    decision: str
    actual_result: str
    success: bool
    metric_value: float
    timestamp: str = None


    def __post_init__(self):

        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()


    def to_dict(self):
        return asdict(self)
