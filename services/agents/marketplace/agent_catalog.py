class AgentCatalog:

    def __init__(self):
        self.agents = {}

    def register(
        self,
        name,
        capabilities
    ):
        self.agents[name] = {
            "name": name,
            "capabilities": capabilities
        }

    def get(self, name):

        return self.agents.get(name)
