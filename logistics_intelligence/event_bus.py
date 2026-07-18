from datetime import datetime


class EventBus:

    def publish(self, event_type, payload):

        return {
            "event_type": event_type,
            "payload": payload,
            "status": "STREAMED",
            "timestamp": datetime.utcnow().isoformat()
        }
