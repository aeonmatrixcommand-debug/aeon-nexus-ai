from services.guardian.execution.authorization import AuthorizationIssuer
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


def test_execution_authority_is_single_use():
    engine = AutonomousExecutionLayer()

    authority = _authority("replay-001")
    decision = _decision("replay-001", authority)

    first = engine.run(decision)
    second = engine.run(decision)

    assert first["status"] == "EXECUTED"

    assert second["status"] == "BLOCKED"
    assert second["reason"] == "EXECUTION_AUTHORITY_ALREADY_CONSUMED"
    assert second.get("execution") is None


def test_failed_binding_does_not_consume_authority():
    engine = AutonomousExecutionLayer()

    authority = _authority("binding-001")

    invalid = _decision(
        "binding-001",
        authority,
        action="TRANSFER_STOCK",
    )

    valid = _decision(
        "binding-001",
        authority,
        action="ALLOCATE_STOCK",
    )

    blocked = engine.run(invalid)
    executed = engine.run(valid)

    assert blocked["status"] == "BLOCKED"
    assert blocked.get("execution") is None

    assert executed["status"] == "EXECUTED"
    assert executed["execution"]["status"] == "EXECUTED"


def test_separate_authorities_for_same_decision_are_independent():
    engine = AutonomousExecutionLayer()

    first_authority = _authority("independent-001")
    second_authority = _authority("independent-001")

    first = engine.run(
        _decision("independent-001", first_authority)
    )

    second = engine.run(
        _decision("independent-001", second_authority)
    )

    assert first["status"] == "EXECUTED"
    assert second["status"] == "EXECUTED"

    assert (
        first_authority.authorization_id
        != second_authority.authorization_id
    )
