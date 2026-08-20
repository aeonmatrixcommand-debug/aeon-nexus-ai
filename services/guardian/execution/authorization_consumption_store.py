from threading import Lock


class _InMemoryAtomicBackend:
    """
    Process-local atomic backend.

    The backend owns both consumption state and synchronization.
    This preserves the existing default behavior while allowing
    independently-created store adapters to share another backend.
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


class InMemoryAuthorizationConsumptionStore:
    """
    Authorization-consumption store adapter.

    By default, each instance uses its own process-local atomic backend.

    A backend may be injected when multiple store instances must share
    the same atomic consumption boundary.

    Durable or distributed implementations must provide atomic
    try_consume() semantics at the backend itself.
    """

    def __init__(self, backend=None):
        self._backend = (
            backend
            if backend is not None
            else _InMemoryAtomicBackend()
        )

    @staticmethod
    def _validate_authorization_id(authorization_id):
        if not authorization_id:
            raise ValueError("AUTHORIZATION_ID_REQUIRED")

    def is_consumed(self, authorization_id):
        self._validate_authorization_id(authorization_id)
        return self._backend.is_consumed(authorization_id)

    def try_consume(self, authorization_id):
        self._validate_authorization_id(authorization_id)
        return self._backend.try_consume(authorization_id)
