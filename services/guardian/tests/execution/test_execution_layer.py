from services.guardian.execution.authorization import AuthorizationIssuer
from services.guardian.execution.execution_layer import AutonomousExecutionLayer


def test_execution_layer():
    engine = AutonomousExecutionLayer()

    decision_id = "decision-execution-layer-001"
    action = "ALLOCATE_STOCK"

    authority = AuthorizationIssuer().issue(
        decision_id=decision_id,
        action=action,
        policy_status="APPROVED",
        approval_status="APPROVED",
    )

    result = engine.run({
        "decision_id": decision_id,
        "action": action,
        "confidence": 0.94,
        "risk_score": 0.10,
        "execution_authority": authority,
    })

    assert result["status"] == "EXECUTED"
    assert result["execution"]["status"] == "EXECUTED"

    assert result["authorization"]["authorization_id"] == (
        authority.authorization_id
    )
    assert result["authorization"]["decision_id"] == decision_id
    assert result["authorization"]["action"] == action
