from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Lock

from services.guardian.execution.authorization import AuthorizationIssuer
from services.guardian.execution.execution_layer import AutonomousExecutionLayer


class CoordinatedAtomicConsumptionRegistry:
    """
    Test double implementing the new atomic claim contract.

    Both callers arrive at try_consume concurrently, but the lock
    permits exactly one successful claim.
    """

    def __init__(self, parties=2):
        self._consumed = set()
        self._arrival_barrier = Barrier(parties)
        self._lock = Lock()

    def try_consume(self, authorization_id):
        if not authorization_id:
            raise ValueError("AUTHORIZATION_ID_REQUIRED")

        self._arrival_barrier.wait()

        with self._lock:
            if authorization_id in self._consumed:
                return False

            self._consumed.add(authorization_id)
            return True


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


def test_authority_claim_is_atomic_before_execution():
    engine = AutonomousExecutionLayer()

    engine.authorization_consumption = (
        CoordinatedAtomicConsumptionRegistry(parties=2)
    )

    authority = _authority("atomic-green-001")
    decision = _decision("atomic-green-001", authority)

    start = Barrier(2)

    def execute():
        start.wait()
        return engine.run(decision)

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [
            pool.submit(execute),
            pool.submit(execute),
        ]
        results = [future.result(timeout=5) for future in futures]

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
    assert len(blocked) == 1, results

    assert blocked[0]["reason"] == (
        "EXECUTION_AUTHORITY_ALREADY_CONSUMED"
    )
