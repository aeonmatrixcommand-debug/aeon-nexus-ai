from datetime import datetime


class AuditTrail:

    def record(self, event):

        return {
            "audit": event,
            "timestamp": datetime.utcnow().isoformat()
        }
