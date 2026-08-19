from services.guardian.execution.authorization import AuthorizationIssuer
from services.guardian.execution.execution_layer import AutonomousExecutionLayer


def _issue_authority(decision_id, action):
    return AuthorizationIssuer().issue(
        decision_id=decision_id,
        action=action,
        policy_status="APPROVED",
        approval_status="APPROVED",
    )


def test_boolean_authorization_must_not_execute():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "decision_id": "decision-001",
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.10,
        "execution_authorized": True,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_valid_authority_allows_execution():
    engine = AutonomousExecutionLayer()

    decision_id = "decision-002"
    action = "ALLOCATE_STOCK"

    authority = _issue_authority(decision_id, action)

    result = engine.run({
        "decision_id": decision_id,
        "action": action,
        "confidence": 0.99,
        "risk_score": 0.10,
        "execution_authority": authority,
    })

    assert result["status"] == "EXECUTED"
    assert result["execution"]["status"] == "EXECUTED"


def test_authority_bound_to_different_action_must_fail_closed():
    engine = AutonomousExecutionLayer()

    authority = _issue_authority(
        "decision-003",
        "ALLOCATE_STOCK",
    )

    result = engine.run({
        "decision_id": "decision-003",
        "action": "DELETE_ORDER",
        "confidence": 0.99,
        "risk_score": 0.10,
        "execution_authority": authority,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_authority_bound_to_different_decision_must_fail_closed():
    engine = AutonomousExecutionLayer()

    authority = _issue_authority(
        "decision-original",
        "ALLOCATE_STOCK",
    )

    result = engine.run({
        "decision_id": "decision-substituted",
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.10,
        "execution_authority": authority,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_missing_authority_must_fail_closed():
    engine = AutonomousExecutionLayer()

    result = engine.run({
        "decision_id": "decision-004",
        "action": "ALLOCATE_STOCK",
        "confidence": 0.99,
        "risk_score": 0.10,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"


def test_authority_cannot_override_high_risk_policy():
    engine = AutonomousExecutionLayer()

    decision_id = "decision-005"
    action = "ALLOCATE_STOCK"

    authority = _issue_authority(decision_id, action)

    result = engine.run({
        "decision_id": decision_id,
        "action": action,
        "confidence": 0.99,
        "risk_score": 0.95,
        "execution_authority": authority,
    })

    assert result.get("status") != "EXECUTED"
    assert result.get("execution", {}).get("status") != "EXECUTED"
