from dataclasses import dataclass


@dataclass
class AgentCapability:

    name: str
    domain: str
    risk_level: str

