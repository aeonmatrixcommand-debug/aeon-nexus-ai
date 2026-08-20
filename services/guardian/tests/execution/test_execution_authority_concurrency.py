from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

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


def test_same_authority_cannot_execute_concurrently():
    engine = AutonomousExecutionLayer()

    authority = _authority("concurrent-001")
    decision = _decision("concurrent-001", authority)

    workers = 16
    barrier = Barrier(workers)

    def execute():
        barrier.wait()
        return engine.run(decision)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda _: execute(), range(workers)))

    executed = [
        result
        for result in results
        if result["status"] == "EXECUTED"
    ]

    blocked = [
        result
        for result in results
        if result["status"] == "BLOCKED"
    ]

    assert len(executed) == 1, results
    assert len(blocked) == workers - 1, results

    assert all(
        result["reason"] == "EXECUTION_AUTHORITY_ALREADY_CONSUMED"
        for result in blocked
    )
