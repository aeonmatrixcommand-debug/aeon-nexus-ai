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


from google.api_core.exceptions import Aborted
from google.cloud import datastore


class DatastoreAuthorizationConsumptionStore:
    """
    Google Cloud Datastore authorization-consumption store.

    Atomicity belongs to the Datastore transaction boundary.

    An authorization ID is represented by a deterministic entity key.
    The first transaction that observes the key as absent creates the
    consumption marker. Later transactions observe the existing marker
    and return False.

    A client must be injected explicitly so infrastructure selection,
    project configuration, credentials, and lifecycle remain outside
    this security primitive.
    """

    KIND = "GuardianAuthorizationConsumption"

    def __init__(self, client):
        if client is None:
            raise ValueError("DATASTORE_CLIENT_REQUIRED")

        self._client = client

    @staticmethod
    def _validate_authorization_id(authorization_id):
        if not authorization_id:
            raise ValueError("AUTHORIZATION_ID_REQUIRED")

    def _key(self, authorization_id):
        return self._client.key(
            self.KIND,
            authorization_id,
        )

    def is_consumed(self, authorization_id):
        self._validate_authorization_id(authorization_id)

        key = self._key(authorization_id)

        return self._client.get(key) is not None

    def try_consume(self, authorization_id):
        self._validate_authorization_id(authorization_id)

        key = self._key(authorization_id)

        max_attempts = 5

        for attempt in range(max_attempts):
            try:
                with self._client.transaction() as transaction:
                    existing = self._client.get(
                        key,
                        transaction=transaction,
                    )

                    if existing is not None:
                        return False

                    entity = datastore.Entity(key=key)
                    entity["authorization_id"] = authorization_id
                    entity["consumed"] = True

                    transaction.put(entity)

                    return True

            except Aborted:
                if attempt == max_attempts - 1:
                    raise

        raise RuntimeError(
            "DATASTORE_CONTENTION_RETRY_EXHAUSTED"
        )
