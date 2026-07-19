
class AgentRegistry:


    def __init__(self):

        self.agents = {}


    def register(
        self,
        name,
        capability
    ):

        self.agents[name]={
            "capability":capability,
            "status":"READY"
        }


    def list_agents(self):

        return self.agents
