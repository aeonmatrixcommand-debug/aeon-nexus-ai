from services.guardian.execution.authorization import AuthorizationIssuer
from services.guardian.execution.execution_layer import AutonomousExecutionLayer
from services.guardian.execution.authorization_consumption import (
    AuthorizationConsumptionRegistry,
)


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


def test_consumption_survives_registry_recreation():
    """
    Durable-store contract:

    Consuming an authorization must survive recreation of the
    registry object when both registries use the same backend.

    This test intentionally describes behavior that the current
    in-memory registry cannot provide.
    """

    backend = {}

    registry_a = AuthorizationConsumptionRegistry(
        backend=backend
    )

    authority = _authority("durable-001")
    decision = _decision("durable-001", authority)

    engine_a = AutonomousExecutionLayer(
        authorization_consumption=registry_a
    )

    first = engine_a.run(decision)

    assert first["status"] == "EXECUTED"

    # Simulate process / execution-layer recreation.
    registry_b = AuthorizationConsumptionRegistry(
        backend=backend
    )

    engine_b = AutonomousExecutionLayer(
        authorization_consumption=registry_b
    )

    second = engine_b.run(decision)

    assert second["status"] == "BLOCKED"
    assert second["reason"] == (
        "EXECUTION_AUTHORITY_ALREADY_CONSUMED"
    )
    assert second.get("execution") is None
