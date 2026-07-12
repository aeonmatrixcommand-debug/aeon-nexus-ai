from services.decision_engine.runtime import AIDecisionEngine


def test_high_risk_decision():

    engine = AIDecisionEngine()

    result = engine.analyze_scenario({
        "risk": 95
    })

    assert result["decision"] == "ACTION_REQUIRED"
    assert result["priority"] == "HIGH"


def test_business_simulation():

    engine = AIDecisionEngine()

    result = engine.simulate_business_impact(
        "inventory_rebalance"
    )

    assert result["confidence"] == "95%"
    assert result["profit_impact"] == "+5%"
