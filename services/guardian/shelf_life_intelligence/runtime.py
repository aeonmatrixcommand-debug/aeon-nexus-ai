class ShelfLifeIntelligence:

    def analyze(self, item):
        days = item.get("days_remaining", 0)

        return {
            "risk": "critical" if days <= 3 else "normal",
            "days_remaining": days
        }
