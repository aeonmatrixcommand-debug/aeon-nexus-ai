from services.agent.memory.adaptive_memory import AdaptiveMemory


def test_agent_memory_store():
    memory = AdaptiveMemory()

    memory.remember(
        task="inventory prediction",
        action="optimize reorder",
        outcome="improved accuracy",
        score=0.95,
    )

    assert len(memory.recall()) == 1
    assert memory.recall()[0].score == 0.95
