from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class AgentMessage:
    sender: str
    receiver: str
    intent: str
    payload: dict
    created_at: datetime = datetime.now(UTC)
