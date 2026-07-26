from src.intelligence.learning.feedback_loop import (
    FeedbackLoop,
)

from src.intelligence.executive.intelligence import (
    ExecutiveIntelligence,
)

from src.intelligence.executive.decision_trace import (
    DecisionTrace,
)


def test_autonomous_closed_loop():

    feedback = FeedbackLoop().evaluate(
        "ACTION-001",
        "completed",
        0.95,
    )

    assert feedback.improvement_score == 0.95

    executive = ExecutiveIntelligence().summarize(
        "reroute shipment"
    )

    assert executive["executive_ready"]

    trace = DecisionTrace().record(
        "reroute shipment",
        0.91,
    )

    assert trace["explainable"]
