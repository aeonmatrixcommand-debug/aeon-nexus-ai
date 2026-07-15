
from services.agents.learning.agent_learning import (
    AgentLearningEngine
)


def test_agent_learning_record():

    engine = AgentLearningEngine()

    engine.record_result(
        "wms-agent",
        "task-001",
        True,
        0.95
    )

    score = engine.evaluate_performance(
        "wms-agent"
    )

    assert score == 0.95



def test_agent_learning_feedback():

    engine = AgentLearningEngine()

    engine.record_result(
        "sales-agent",
        "task-001",
        True,
        0.9
    )

    feedback = engine.generate_feedback(
        "sales-agent"
    )

    assert feedback == "Excellent performance"

