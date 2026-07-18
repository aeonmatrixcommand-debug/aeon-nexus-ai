class InventoryOptimizer:

    def optimize(self, forecast):

        if forecast["demand_level"] == "HIGH_DEMAND":
            action = "INCREASE_STOCK"

        elif forecast["demand_level"] == "LOW_DEMAND":
            action = "REDUCE_STOCK"

        else:
            action = "MAINTAIN_STOCK"

        return {
            "optimization_action": action,
            "status": "EXECUTION_READY"
        }
