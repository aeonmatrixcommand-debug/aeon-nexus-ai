class OpportunityEngine:
    """
    Detect business opportunities from digital twin state.
    """

    def detect(self, twin_state):

        opportunities = []

        signals = getattr(twin_state, "signals", {})

        if signals.get("demand_growth", 0) > 0.2:
            opportunities.append({
                "type": "capacity_expansion",
                "reason": "Demand growth detected",
                "impact": "Revenue opportunity"
            })

        if signals.get("inventory_risk") == "high":
            opportunities.append({
                "type": "inventory_optimization",
                "reason": "Inventory imbalance",
                "impact": "Waste reduction"
            })

        return opportunities
