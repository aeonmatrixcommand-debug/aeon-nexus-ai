from dataclasses import dataclass
from typing import Dict


@dataclass
class AgentResult:
    success: bool
    agent_name: str
    output: Dict
    message: str = ""
