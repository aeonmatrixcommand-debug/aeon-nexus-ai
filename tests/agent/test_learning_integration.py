from services.agent.learning.integration import AgentLearningIntegrator


def test_agent_learning_integration():

    integrator = AgentLearningIntegrator()

    state = integrator.integrate(
        agent_id="AEON-001",
        memory_score=0.9,
        collaboration_score=0.85,
        reward_score=0.95,
        evolution_score=0.88,
    )

    assert state.agent_id == "AEON-001"
    assert state.reward_score == 0.95
