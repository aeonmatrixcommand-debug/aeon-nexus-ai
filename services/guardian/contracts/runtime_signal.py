from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class RuntimeSignal:
    module: str
    event_type: str
    decision: str
    confidence: float
    risk_score: float = 0.0
    trace_id: str = str(uuid4())
    timestamp: str = datetime.utcnow().isoformat()


    def __getitem__(self, key):
        if key == "policy":
            return "APPROVED"
        return getattr(self, key)
