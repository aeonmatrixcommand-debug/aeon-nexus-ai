from datetime import datetime, timezone


class AuditEngine:
    """
    Record AI governance history.
    """

    def record(self, action, result):

        return {
            "timestamp":
                datetime.now(timezone.utc).isoformat(),

            "action":
                action,

            "result":
                result
        }
