class ImpactEngine:
    def calculate(self, scenario):
        context = scenario.get("context", {})

        demand = context.get("demand", 0)
        inventory = context.get("inventory", 0)

        return {
            "inventory_gap": demand - inventory,
            "risk": "HIGH" if demand > inventory else "LOW",
            "impact_score": min(abs(demand - inventory) * 10, 100)
        }
