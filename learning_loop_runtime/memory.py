from datetime import datetime


class EnterpriseMemory:

    def __init__(self):
        self.memory = []


    def store(self, event, outcome):

        record = {
            "event": event,
            "outcome": outcome,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.memory.append(record)

        return record


    def recall(self):

        return self.memory
