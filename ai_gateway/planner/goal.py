from datetime import datetime


class Goal:

    def __init__(self, name, objective):
        self.name = name
        self.objective = objective
        self.created = datetime.utcnow().isoformat()


    def to_dict(self):
        return {
            "name": self.name,
            "objective": self.objective,
            "created": self.created
        }
