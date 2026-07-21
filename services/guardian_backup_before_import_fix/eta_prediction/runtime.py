class ETAPredictionEngine:

    def predict(self, shipment):
        delay = shipment.get("delay", 0)

        return {
            "eta_status": "delayed" if delay > 30 else "on_time",
            "delay_minutes": delay
        }
