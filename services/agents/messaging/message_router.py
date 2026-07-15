from services.agents.core.message import AgentMessage


class AgentMessageRouter:

    def __init__(self, registry):
        self.registry = registry


    def route(self, message: AgentMessage):

        agent = self.registry.get_agent(
            message.receiver
        )

        return agent
