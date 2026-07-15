from digital_twin.decision.recommendation_engine import RecommendationEngine


def test_recommendation():

    simulations = [
        {
            "cost": 12000,
            "risk_reduction": 0.85
        },
        {
            "cost": 5000,
            "risk_reduction": 0.60
        }
    ]

    result = RecommendationEngine().recommend(simulations)

    assert result["risk_reduction"] == 0.85
