from datetime import datetime


class TelemetryTower:

    def collect(self, event):

        return {
            "event": event,
            "telemetry_status": "ACTIVE",
            "data_quality": "HIGH",
            "timestamp": datetime.utcnow().isoformat()
        }
