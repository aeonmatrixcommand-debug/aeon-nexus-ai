from services.guardian.action_recommendation.runtime import ExecutiveActionRecommendation


def test_action_recommendation():
    result = ExecutiveActionRecommendation().recommend(
        {"risk": 0.9}
    )

    assert result["action"] == "intervene"

    result = ExecutiveActionRecommendation().recommend(
        {"risk": 0.1}
    )

    assert result["action"] == "observe"
