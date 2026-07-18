from datetime import datetime


class TelemetryStream:

    def publish(self, event):

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "status": "RECEIVED"
        }
