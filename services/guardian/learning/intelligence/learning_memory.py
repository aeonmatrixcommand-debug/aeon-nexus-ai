from datetime import datetime


class LearningMemory:
    def __init__(self):
        self.events = []

    def store(self, event):
        event["timestamp"] = datetime.utcnow().isoformat()
        self.events.append(event)
        return event

    def history(self):
        return self.events


memory = LearningMemory()
