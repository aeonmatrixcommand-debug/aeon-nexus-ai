from threading import Lock


class AuthorizationConsumptionRegistry:
    """
    Tracks execution authorities consumed by this execution boundary.

    try_consume() is the atomic claim operation. Exactly one caller
    can successfully claim a given authorization_id per registry.
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

    def consume(self, authorization_id):
        """
        Backward-compatible wrapper.

        Returns True only for the first successful consumption.
        """
        return self.try_consume(authorization_id)
