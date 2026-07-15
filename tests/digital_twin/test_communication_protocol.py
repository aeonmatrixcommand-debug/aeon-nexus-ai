from digital_twin.agents.communication_protocol import CommunicationProtocol


def test_communication():

    result = CommunicationProtocol().send(
        "risk_agent",
        "decision_agent",
        "cold_chain_risk"
    )

    assert result["status"] == "delivered"
