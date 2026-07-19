class SimulationEngine:
    """
    Simulate possible outcomes before execution.
    """

    def simulate(self, decision):

        action = decision["action"]

        if action == "move_to_backup_storage":
            return {
                "cost": 12000,
                "risk_reduction": 0.85,
                "sla_protection": "high"
            }

        if action == "optimize_capacity":
            return {
                "cost": 5000,
                "risk_reduction": 0.60,
                "sla_protection": "medium"
            }

        return {
            "cost": 0,
            "risk_reduction": 0,
            "sla_protection": "unknown"
        }
