class Telemetry:
    def collect(self, metric: dict) -> dict:
        return {
            "telemetry_status": "received",
            "metric": metric
        }
