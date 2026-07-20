from datetime import datetime


class LearningBridge:

    def __init__(self):
        self.events = []

    def record(self, event):
        payload = {
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(payload)

        return payload

    def get_events(self):
        return self.events
