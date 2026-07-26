from services.agent.evolution.evolution_engine import (
    AgentEvolutionEngine,
)


def test_agent_evolution_signal():
    engine = AgentEvolutionEngine()

    signal = engine.evaluate(
        agent_id="AEON-001",
        outcome="successful_task",
        score=0.95,
    )

    assert signal.agent_id == "AEON-001"
    assert signal.score == 0.95
    assert len(engine.signals) == 1
