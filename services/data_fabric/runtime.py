from datetime import datetime


class EnterpriseEventBus:

    def __init__(self):
        self.events = []
        self.status = "ONLINE"


    def publish(self, event_type, payload):

        event = {
            "type": event_type,
            "payload": payload,
            "timestamp": datetime.now().isoformat(),
            "status": "RECEIVED"
        }

        self.events.append(event)

        return event


    def consume_latest(self):

        if not self.events:
            return None

        return self.events[-1]


    def governance_log(self):

        return {
            "event_count": len(self.events),
            "audit": "ENABLED",
            "security": "ACTIVE"
        }
