from datetime import datetime
import uuid


class EventBus:

    def __init__(self):
        self.events = []


    def publish(
        self,
        event_type,
        payload
    ):

        event = {
            "id": str(uuid.uuid4()),
            "type": event_type,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }

        self.events.append(event)

        return event


    def history(self):
        return self.events
