class ValueRecoveryEngine:

    def __init__(self):
        self.name = "Value Recovery Intelligence"

    def analyze_loss(self, data):

        waste = data.get("waste_percent", 0)
        sla = data.get("sla_percent", 100)

        if waste > 20:
            return {
                "risk": "HIGH",
                "recovery_action": "OPTIMIZE_INVENTORY",
                "value_recovery": "+15%"
            }

        if sla < 90:
            return {
                "risk": "MEDIUM",
                "recovery_action": "ROUTE_OPTIMIZATION",
                "value_recovery": "+8%"
            }

        return {
            "risk": "LOW",
            "recovery_action": "MONITOR",
            "value_recovery": "+0%"
        }


    def governance_record(self, result):

        return {
            "engine": self.name,
            "decision": result["recovery_action"],
            "audit": "ENABLED"
        }
