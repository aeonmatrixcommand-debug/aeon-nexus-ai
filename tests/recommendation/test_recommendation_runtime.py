from services.guardian.recommendation_runtime.runtime import RecommendationRuntime


def test_recommend_execute():
    rt = RecommendationRuntime()
    result = rt.recommend({"risk_score": 0.1})

    assert result["action"] == "execute"


def test_recommend_monitor():
    rt = RecommendationRuntime()
    result = rt.recommend({"risk_score": 0.5})

    assert result["action"] == "monitor"


def test_recommend_review():
    rt = RecommendationRuntime()
    result = rt.recommend({"risk_score": 0.9})

    assert result["action"] == "review"
