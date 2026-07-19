class TwinSimulator:

    def simulate(self, state):

        gap = state["demand"] - state["inventory"]

        return {
            "inventory_gap": gap,
            "impact": "HIGH" if gap > 0 else "NORMAL"
        }
