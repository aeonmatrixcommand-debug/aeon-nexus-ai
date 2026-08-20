from threading import Lock


class InMemoryAuthorizationConsumptionStore:
    """
    Atomic in-memory authorization-consumption store.

    Multiple registry instances may share this store.

    This implementation is process-local and is NOT a durable
    distributed store.
    """

    def __init__(self):
        self._consumed = set()
        self._lock = Lock()

    def is_consumed(self, authorization_id):
        if not authorization_id:
            raise ValueError("AUTHORIZATION_ID_REQUIRED")

        with self._lock:
            return authorization_id in self._consumed

    def try_consume(self, authorization_id):
        if not authorization_id:
            raise ValueError("AUTHORIZATION_ID_REQUIRED")

        with self._lock:
            if authorization_id in self._consumed:
                return False

            self._consumed.add(authorization_id)
            return True
