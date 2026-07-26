from services.agent.collaboration.message import AgentMessage


def test_agent_message_creation():
    message = AgentMessage(
        sender="AEON-001",
        receiver="AEON-002",
        intent="share_memory",
        payload={"signal": "learning"}
    )

    assert message.sender == "AEON-001"
    assert message.receiver == "AEON-002"
