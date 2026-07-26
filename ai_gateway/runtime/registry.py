class AgentRegistry:

    def __init__(self):
        self.agents = {}


    def register(self, agent_id, data):

        self.agents[agent_id] = data


    def list(self):

        return self.agents
