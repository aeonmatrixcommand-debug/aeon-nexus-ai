from datetime import datetime


class AIAuditTrail:

    def log(self, action):

        return {
            "audit": "RECORDED",
            "action": action,
            "timestamp": datetime.utcnow().isoformat()
        }
