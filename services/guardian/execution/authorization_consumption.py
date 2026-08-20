from services.guardian.execution.authorization_consumption_store import (
    InMemoryAuthorizationConsumptionStore,
)


class AuthorizationConsumptionRegistry:
    """
    Execution-authority consumption boundary.

    The registry delegates atomic consumption to a store.

    A store may be shared by multiple registry instances.
    """

    def __init__(self, store=None, backend=None):
        if store is not None and backend is not None:
            raise ValueError(
                "AUTHORIZATION_CONSUMPTION_STORE_CONFLICT"
            )

        # Compatibility with the RED contract that introduced
        # backend injection. A dict backend is converted into a
        # shared store held by the backend itself.
        if backend is not None:
            if not isinstance(backend, dict):
                raise TypeError(
                    "AUTHORIZATION_CONSUMPTION_BACKEND_INVALID"
                )

            store = backend.get(
                "_authorization_consumption_store"
            )

            if store is None:
                store = InMemoryAuthorizationConsumptionStore()
                backend[
                    "_authorization_consumption_store"
                ] = store

        self._store = (
            store
            if store is not None
            else InMemoryAuthorizationConsumptionStore()
        )

    def is_consumed(self, authorization_id):
        return self._store.is_consumed(authorization_id)

    def try_consume(self, authorization_id):
        return self._store.try_consume(authorization_id)

    def consume(self, authorization_id):
        """
        Backward-compatible wrapper.

        Returns True only for the first successful consumption.
        """
        return self.try_consume(authorization_id)
