from services.agent.learning.feedback import AgentFeedback


def test_agent_feedback_creation():
    feedback = AgentFeedback(
        agent_id="AEON-001",
        action="inventory_prediction",
        reward=0.95,
        context={"accuracy": "high"}
    )

    assert feedback.agent_id == "AEON-001"
    assert feedback.reward == 0.95
