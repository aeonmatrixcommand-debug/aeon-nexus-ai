from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AgentTask:

    task_id: str
    capability: str
    payload: Dict[str, Any]

