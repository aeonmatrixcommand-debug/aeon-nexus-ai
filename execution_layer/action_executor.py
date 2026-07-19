class ActionExecutor:

    def execute(self, decision):

        if decision["execution"] == "AUTHORIZED":
            return {
                "status": "EXECUTED",
                "action": decision["policy"]["decision"]
            }

        if decision["execution"] == "WAITING_HUMAN_APPROVAL":
            return {
                "status": "PENDING_APPROVAL",
                "action": decision["policy"]["decision"]
            }

        return {
            "status": "BLOCKED",
            "action": decision["policy"]["decision"]
        }
