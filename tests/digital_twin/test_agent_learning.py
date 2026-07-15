from digital_twin.agents.agent_learning import AgentLearning


def test_agent_learning():

    result = AgentLearning().learn(
        "reroute_vehicle",
        "sla_recovered"
    )

    assert result["learning"] == "updated"
