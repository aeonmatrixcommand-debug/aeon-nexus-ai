from datetime import datetime, timezone


class AuditReasoning:
    """
    Store AI decision reasoning history.
    """

    def record(self, explanation):

        return {
            "timestamp":
                datetime.now(timezone.utc).isoformat(),

            "decision":
                explanation["decision"],

            "reason":
                explanation["reason"],

            "evidence":
                explanation["evidence"]
        }
