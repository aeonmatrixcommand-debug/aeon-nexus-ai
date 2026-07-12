from services.guardian.decision_intelligence.runtime import DecisionIntelligence


def test_decision_intelligence():
    assert DecisionIntelligence().evaluate(
        {"risk_score": 0.9}
    )["decision"] == "escalate"

    assert DecisionIntelligence().evaluate(
        {"risk_score": 0.6}
    )["priority"] == "high"

    assert DecisionIntelligence().evaluate(
        {"risk_score": 0.1}
    )["decision"] == "approve"
