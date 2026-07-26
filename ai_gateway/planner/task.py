from datetime import datetime


class Task:

    def __init__(self, name, action):
        self.name = name
        self.action = action
        self.status = "PENDING"
        self.created = datetime.utcnow().isoformat()


    def complete(self):
        self.status = "COMPLETED"


    def to_dict(self):
        return {
            "name": self.name,
            "action": self.action,
            "status": self.status,
            "created": self.created
        }
