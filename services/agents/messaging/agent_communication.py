from services.agents.core.message import AgentMessage


class AgentCommunication:

    def __init__(
        self,
        event_bus,
        router
    ):
        self.event_bus = event_bus
        self.router = router


    def send(
        self,
        message: AgentMessage
    ):

        self.event_bus.publish(message)

        return self.router.route(message)
