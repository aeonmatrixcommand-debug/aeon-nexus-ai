from services.agents.core.message import AgentMessage
from services.agents.messaging.event_bus import AgentEventBus
from services.agents.messaging.agent_communication import AgentCommunication


class MockRegistry:

    def get_agent(self, name):

        return {
            "name": name,
            "status": "ready"
        }


class MockRouter:

    def route(self, message):

        return {
            "agent": message.receiver,
            "received": True
        }


def test_agent_message_publish():

    bus = AgentEventBus()

    message = AgentMessage(
        sender="demand_agent",
        receiver="inventory_agent",
        message_type="REQUEST",
        payload={
            "forecast": "increase"
        }
    )

    bus.publish(message)

    events = bus.get_events()

    assert len(events) == 1
    assert events[0].sender == "demand_agent"
    assert events[0].receiver == "inventory_agent"


def test_agent_communication_route():

    communication = AgentCommunication(
        event_bus=AgentEventBus(),
        router=MockRouter()
    )

    message = AgentMessage(
        sender="sales_agent",
        receiver="wms_agent",
        message_type="REQUEST",
        payload={
            "sku": "A100"
        }
    )

    result = communication.send(message)

    assert result["agent"] == "wms_agent"
    assert result["received"] is True
