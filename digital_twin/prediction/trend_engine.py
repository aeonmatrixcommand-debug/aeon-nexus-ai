class TrendEngine:
    """
    Analyze operational trends from digital twin signals.
    """

    def analyze(self, signals):

        result = {
            "trend": "stable",
            "risk": "low",
            "explanation": []
        }

        if signals.get("demand_growth", 0) > 0.3:
            result["trend"] = "growth"
            result["explanation"].append(
                "Demand increasing rapidly"
            )

        if signals.get("capacity", 0) > 0.8:
            result["risk"] = "capacity_pressure"
            result["explanation"].append(
                "Capacity utilization is high"
            )

        return result
