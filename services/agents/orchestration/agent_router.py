class AgentRouter:

    def __init__(self, registry):
        self.registry = registry

    def route(self, capability: str):

        for agent in self.registry.list_agents():

            if capability in agent.capabilities:
                return agent

        return None
