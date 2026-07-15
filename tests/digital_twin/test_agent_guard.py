from digital_twin.agents.agent_guard import AgentGuard


def test_agent_guard():

    result = AgentGuard().validate(
        "reroute_vehicle"
    )

    assert result["status"] == "allowed"
