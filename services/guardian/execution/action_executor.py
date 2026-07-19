from datetime import datetime


class ActionExecutor:

    def execute(self, action):

        return {
            "action": action,
            "status": "EXECUTED",
            "executed_at": datetime.utcnow().isoformat()
        }
