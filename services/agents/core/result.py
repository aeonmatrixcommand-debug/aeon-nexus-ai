from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class AgentResult:

    success: bool
    agent_name: str
    output: Dict[str, Any]
    message: str = ""

