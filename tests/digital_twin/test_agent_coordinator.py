from digital_twin.agents.agent_coordinator import AgentCoordinator


def test_agent_coordination():

    result = AgentCoordinator().coordinate(
        "cold_chain_analysis"
    )

    assert result["status"] == "coordinated"
