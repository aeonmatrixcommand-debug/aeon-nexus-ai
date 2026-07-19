import json
from datetime import datetime


class EnterpriseMemory:

    def __init__(self):
        self.memory = []

    def save(self, event):

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event
        }

        self.memory.append(record)

        with open(
            "enterprise_memory/runtime_memory.json",
            "w"
        ) as f:
            json.dump(
                self.memory,
                f,
                indent=2
            )

        return record


    def recall(self):

        return self.memory
