from datetime import datetime


class DemandForecastEngine:

    def predict(self, sku, history):

        avg = sum(history) / len(history)

        return {
            "sku": sku,
            "forecast_demand": round(avg * 1.15, 2),
            "confidence": "HIGH",
            "generated_at": datetime.utcnow().isoformat()
        }
