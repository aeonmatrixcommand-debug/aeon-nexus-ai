from ai_gateway.marketplace.agent_profile import AgentProfile
from ai_gateway.marketplace.reputation import AgentReputation



class AgentMarketplace:


    def __init__(self):

        self.agents = {}
        self.reputation = AgentReputation()



    def publish(
        self,
        agent_id,
        capability
    ):

        profile = AgentProfile(
            agent_id,
            capability
        )

        self.agents[agent_id] = profile

        return profile.to_dict()



    def search(
        self,
        capability
    ):

        return [
            agent.to_dict()
            for agent in self.agents.values()
            if agent.capability == capability
        ]



    def rate(
        self,
        agent_id,
        score
    ):

        agent = self.agents[agent_id]

        agent.update_rating(
            score
        )

        return self.reputation.evaluate(
            agent
        )
