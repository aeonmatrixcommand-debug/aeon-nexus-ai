from services.value_recovery.runtime import ValueRecoveryEngine


def test_high_waste_recovery():

    engine = ValueRecoveryEngine()

    result = engine.analyze_loss({
        "waste_percent": 30
    })

    assert result["risk"] == "HIGH"
    assert result["recovery_action"] == "OPTIMIZE_INVENTORY"


def test_sla_recovery():

    engine = ValueRecoveryEngine()

    result = engine.analyze_loss({
        "sla_percent": 80
    })

    assert result["recovery_action"] == "ROUTE_OPTIMIZATION"


def test_governance():

    engine = ValueRecoveryEngine()

    result = engine.governance_record({
        "recovery_action": "MONITOR"
    })

    assert result["audit"] == "ENABLED"
