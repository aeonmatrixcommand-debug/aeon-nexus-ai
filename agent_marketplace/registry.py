class AgentRegistry:

    def __init__(self):
        self.agents = []

    def register(self, name, capability):

        self.agents.append({
            "agent": name,
            "capability": capability,
            "status": "ONLINE"
        })

        return self.agents

    def list_agents(self):
        return self.agents
