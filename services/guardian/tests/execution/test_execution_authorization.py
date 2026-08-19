from services.guardian.execution.execution_layer import AutonomousExecutionLayer


def test_high_confidence_alone_must_not_authorize_execution():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_missing_authorization_must_fail_closed():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.10,
    })

    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_high_risk_must_not_execute():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.95,
    })

    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_legacy_boolean_authorization_must_not_execute():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "decision_id": "legacy-boolean-001",
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.10,
        "execution_authorized": True,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_legacy_boolean_cannot_override_high_risk_block():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "decision_id": "legacy-boolean-high-risk-001",
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.95,
        "execution_authorized": True,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"
