from digital_twin.agents.agent_memory import AgentMemory


def test_agent_memory():

    memory = AgentMemory()

    result = memory.store(
        "risk_agent",
        "temperature anomaly"
    )

    assert result == "stored"
    assert len(memory.recall()) == 1
