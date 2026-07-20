from services.guardian.integration.learning_gateway import publish_learning
from services.guardian.learning.scoring.decision_score import calculate_score


def test_learning_feedback():
    result = publish_learning({
        "module": "DemandForecast",
        "outcome": "SUCCESS"
    })

    assert "action" in result


def test_decision_score():
    score = calculate_score(
        confidence=0.9,
        success=1,
        risk=0.1
    )

    assert score > 0
