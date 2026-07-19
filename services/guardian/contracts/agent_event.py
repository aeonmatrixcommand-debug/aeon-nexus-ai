from dataclasses import dataclass, asdict
from datetime import datetime
import uuid


@dataclass
class AgentEvent:

    agent_name: str
    task: str
    action: str
    confidence: float
    resource_score: float
    trace_id: str = None
    timestamp: str = None


    def __post_init__(self):

        if self.trace_id is None:
            self.trace_id = str(uuid.uuid4())

        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()


    def to_dict(self):

        return asdict(self)
