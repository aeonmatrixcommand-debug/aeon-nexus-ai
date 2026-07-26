from datetime import datetime


class MemoryStore:

    def __init__(self):
        self.entries = []


    def remember(self, event):

        self.entries.append({
            "timestamp": datetime.utcnow().isoformat(),
            "event": event
        })


    def recall(self):

        return self.entries
