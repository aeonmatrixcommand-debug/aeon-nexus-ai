class ExecutiveFeed:

    def create(self, decision):

        return {
            "executive_signal": True,
            "decision": decision,
            "priority": "HIGH"
        }
