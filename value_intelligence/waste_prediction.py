class WastePredictionEngine:

    def predict(self, inventory):

        risk = "LOW"

        if inventory > 1000:
            risk = "HIGH"

        elif inventory > 500:
            risk = "MEDIUM"

        return {
            "waste_risk": risk,
            "inventory_level": inventory
        }
