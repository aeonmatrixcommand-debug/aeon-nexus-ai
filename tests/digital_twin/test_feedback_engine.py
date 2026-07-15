from digital_twin.learning.feedback_engine import FeedbackEngine


def test_feedback():

    result = FeedbackEngine().evaluate(
        0.90,
        0.85
    )

    assert result["learning_status"] == "captured"
