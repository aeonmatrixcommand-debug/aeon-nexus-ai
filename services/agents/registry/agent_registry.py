from typing import Dict
from .agent_metadata import AgentMetadata


class AgentRegistry:

    def __init__(self):
        self._agents: Dict[str, AgentMetadata] = {}

    def register(self, agent: AgentMetadata):
        self._agents[agent.name] = agent

    def get(self, name: str):
        return self._agents.get(name)

    def list_agents(self):
        return list(self._agents.values())
