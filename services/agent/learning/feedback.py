from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class AgentFeedback:
    agent_id: str
    action: str
    reward: float
    context: dict
    created_at: datetime = datetime.now(UTC)
