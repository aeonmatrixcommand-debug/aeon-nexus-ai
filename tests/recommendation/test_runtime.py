from services.guardian.recommendation_runtime.runtime import RecommendationRuntime

def test_recommendation():
    runtime = RecommendationRuntime()

    result = runtime.recommend({
        "risk_score": 0.2
    })

    assert result["action"] == "execute"
    assert "confidence" in result
