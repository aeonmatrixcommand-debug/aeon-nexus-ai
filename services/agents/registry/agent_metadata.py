from dataclasses import dataclass, field
from typing import List


@dataclass
class AgentMetadata:
    name: str
    version: str
    capabilities: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)
    risk_level: str = "low"
    status: str = "active"
