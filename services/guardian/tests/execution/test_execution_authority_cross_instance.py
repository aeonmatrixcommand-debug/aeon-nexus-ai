from services.guardian.execution.authorization import AuthorizationIssuer
from services.guardian.execution.authorization_consumption import (
    AuthorizationConsumptionRegistry,
)
from services.guardian.execution.execution_layer import AutonomousExecutionLayer


def _authority(decision_id, action="ALLOCATE_STOCK"):
    return AuthorizationIssuer().issue(
        decision_id=decision_id,
        action=action,
        policy_status="APPROVED",
        approval_status="APPROVED",
    )


def _decision(decision_id, authority, action="ALLOCATE_STOCK"):
    return {
        "decision_id": decision_id,
        "action": action,
        "confidence": 0.99,
        "risk_score": 0.10,
        "execution_authority": authority,
    }


def test_same_authority_cannot_execute_across_layers_with_shared_store():
    shared_store = AuthorizationConsumptionRegistry()

    engine_a = AutonomousExecutionLayer(
        authorization_consumption=shared_store
    )
    engine_b = AutonomousExecutionLayer(
        authorization_consumption=shared_store
    )

    authority = _authority("cross-instance-green-001")
    decision = _decision("cross-instance-green-001", authority)

    first = engine_a.run(decision)
    second = engine_b.run(decision)

    executed = [
        result
        for result in (first, second)
        if result["status"] == "EXECUTED"
    ]

    blocked = [
        result
        for result in (first, second)
        if result["status"] == "BLOCKED"
    ]

    assert len(executed) == 1, (first, second)
    assert len(blocked) == 1, (first, second)

    assert blocked[0]["reason"] == (
        "EXECUTION_AUTHORITY_ALREADY_CONSUMED"
    )
