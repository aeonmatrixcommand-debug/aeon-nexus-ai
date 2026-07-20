class RecoveryEngine:

    def analyze(self, event):

        risk = event.get(
            "risk",
            "LOW"
        )

        if risk == "HIGH":
            return {
                "action": "AUTO_RECOVERY",
                "status": "TRIGGERED"
            }

        return {
            "action": "MONITOR",
            "status": "STABLE"
        }
