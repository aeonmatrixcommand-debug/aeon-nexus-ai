from datetime import datetime


class EventMesh:

    def __init__(self):
        self.events = []

    def publish(self, topic, payload):

        event = {
            "topic": topic,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(event)

        return event

    def stream(self):
        return self.events
