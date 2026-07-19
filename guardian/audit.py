from datetime import datetime


class AuditLogger:

    def log(self, action, result):

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "decision": result["policy"]["decision"],
            "execution": result["execution"]
        }

        return record
