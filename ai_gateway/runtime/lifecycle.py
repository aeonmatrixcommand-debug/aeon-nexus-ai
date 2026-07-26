from datetime import datetime


class LifecycleManager:

    def __init__(self):
        self.states = []

    def move(self, state):
        self.states.append({
            "state": state,
            "timestamp": datetime.utcnow().isoformat()
        })

    def history(self):
        return self.states
