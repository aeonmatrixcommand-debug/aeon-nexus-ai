class LogisticsOptimizer:

    def optimize(self, eta):

        if eta["delay_minutes"] > 30:
            action = "REROUTE_AND_REBALANCE"
        else:
            action = "CONTINUE_ROUTE"

        return {
            "optimization": action,
            "status": "READY"
        }
