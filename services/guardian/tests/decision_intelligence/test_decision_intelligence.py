from services.guardian.decision_intelligence.impact_score import ImpactScoreEngine
from services.guardian.decision_intelligence.decision_engine import DecisionIntelligenceEngine
from services.guardian.decision_intelligence.runtime_bridge import DecisionRuntimeBridge


def test_decision_intelligence_flow():

    prediction = {
        "impact_score": 0.9
    }

    risk = {
        "risk_score": 0.1
    }

    impact = ImpactScoreEngine().calculate(
        prediction,
        risk
    )

    decision = DecisionIntelligenceEngine().decide(
        impact
    )

    event = DecisionRuntimeBridge().publish(
        decision
    )

    assert impact["priority"] == "HIGH"
    assert decision["decision"] == "AUTONOMOUS_ACTION"
    assert event["runtime_event"] == "DECISION_CREATED"
