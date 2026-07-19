from datetime import datetime


class TelemetryBus:

    def publish(self, source, event):

        return {
            "source": source,
            "event": event,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "RECEIVED"
        }
