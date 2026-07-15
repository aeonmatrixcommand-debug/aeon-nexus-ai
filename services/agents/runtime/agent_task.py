from dataclasses import dataclass
from typing import Dict


@dataclass
class AgentTask:
    task_id: str
    capability: str
    payload: Dict
    requester: str
