from typing import List

from services.agents.core.message import AgentMessage


class AgentEventBus:

    def __init__(self):
        self.events: List[AgentMessage] = []


    def publish(self, message: AgentMessage):

        self.events.append(message)


    def get_events(self):

        return self.events
