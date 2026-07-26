class FederationRegistry:


    def __init__(self):

        self.agents = {}



    def register(
        self,
        agent_id,
        capability
    ):

        self.agents[agent_id] = {
            "capability": capability,
            "status": "ONLINE"
        }



    def discover(
        self,
        capability
    ):

        return {
            agent_id:data
            for agent_id,data
            in self.agents.items()
            if data["capability"] == capability
        }
