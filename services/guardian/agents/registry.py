class AgentRegistry:

    def __init__(self):
        self.agents = {}

    def register(self, name, capability):
        self.agents[name] = {
            "capability": capability,
            "status": "READY"
        }

    def list_agents(self):
        return self.agents


registry = AgentRegistry()

registry.register(
    "Forecast Agent",
    "Demand Prediction"
)

registry.register(
    "Risk Agent",
    "Risk Assessment"
)

registry.register(
    "Optimization Agent",
    "Resource Optimization"
)
