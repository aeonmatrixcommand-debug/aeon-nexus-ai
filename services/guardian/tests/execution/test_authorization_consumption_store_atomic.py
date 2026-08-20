from concurrent.futures import ThreadPoolExecutor
from threading import Lock

from services.guardian.execution.authorization_consumption_store import (
    InMemoryAuthorizationConsumptionStore,
)


class SharedAtomicBackend:
    """
    Test backend representing state shared by independently-created
    consumption-store adapters.

    The atomic claim primitive belongs to the shared backend boundary.
    This models the semantic required from a future durable/distributed
    implementation without selecting a cloud database yet.
    """

    def __init__(self):
        self._consumed = set()
        self._lock = Lock()

    def is_consumed(self, authorization_id):
        with self._lock:
            return authorization_id in self._consumed

    def try_consume(self, authorization_id):
        with self._lock:
            if authorization_id in self._consumed:
                return False

            self._consumed.add(authorization_id)
            return True


def _build_store(backend):
    """
    Future adapter contract under test.

    Expected RED today because the current in-memory store constructor
    does not accept an injected backend.
    """
    return InMemoryAuthorizationConsumptionStore(
        backend=backend
    )


def test_claim_survives_store_recreation():
    backend = SharedAtomicBackend()

    store_a = _build_store(backend)

    assert store_a.try_consume("persistent-auth-001") is True

    del store_a

    store_b = _build_store(backend)

    assert store_b.try_consume("persistent-auth-001") is False


def test_independent_store_instances_share_consumption_state():
    backend = SharedAtomicBackend()

    store_a = _build_store(backend)
    store_b = _build_store(backend)

    assert store_a.try_consume("persistent-auth-002") is True
    assert store_b.try_consume("persistent-auth-002") is False


def test_concurrent_claim_has_exactly_one_winner():
    backend = SharedAtomicBackend()

    stores = [
        _build_store(backend)
        for _ in range(32)
    ]

    authorization_id = "persistent-auth-race-001"

    def claim(store):
        return store.try_consume(authorization_id)

    with ThreadPoolExecutor(max_workers=32) as pool:
        results = list(pool.map(claim, stores))

    assert results.count(True) == 1, results
    assert results.count(False) == 31, results
