from services.guardian.agents.economy.agent_profile import AgentProfile


class CapabilityRegistry:

    def __init__(self):
        self.agents = []

    def register(self, agent):
        self.agents.append(agent)

    def find(self, skill):
        return [
            a for a in self.agents
            if a.capability == skill
        ]


registry = CapabilityRegistry()

registry.register(
    AgentProfile(
        "Forecast Agent",
        "Demand Intelligence",
        0.94,
        0.01,
        "5m"
    )
)

registry.register(
    AgentProfile(
        "Risk Agent",
        "Risk Intelligence",
        0.91,
        0.02,
        "2m"
    )
)
