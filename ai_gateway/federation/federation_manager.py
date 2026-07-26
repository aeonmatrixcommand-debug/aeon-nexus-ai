from ai_gateway.federation.agent_registry import FederationRegistry
from ai_gateway.federation.collaboration import AgentCollaboration



class FederationManager:


    def __init__(self):

        self.registry = FederationRegistry()
        self.communication = AgentCollaboration()



    def add_agent(
        self,
        agent_id,
        capability
    ):

        self.registry.register(
            agent_id,
            capability
        )



    def delegate(
        self,
        sender,
        capability,
        task
    ):

        targets = self.registry.discover(
            capability
        )


        results = []


        for agent_id in targets:

            results.append(
                self.communication.send(
                    sender,
                    agent_id,
                    task
                )
            )


        return results
