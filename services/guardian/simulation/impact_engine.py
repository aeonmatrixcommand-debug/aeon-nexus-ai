class ImpactEngine:

    def calculate(self, scenario):

        context = scenario.get(
            "context",
            {}
        )

        demand = context.get(
            "demand",
            0
        )

        inventory = context.get(
            "inventory",
            0
        )

        risk = (
            "HIGH"
            if demand > inventory
            else "LOW"
        )

        return {
            "inventory_gap": demand - inventory,
            "risk": risk,
            "impact_score": min(
                abs(demand - inventory) * 10,
                100
            )
        }
