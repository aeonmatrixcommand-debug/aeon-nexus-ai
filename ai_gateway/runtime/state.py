from datetime import datetime


class AgentState:

    def __init__(self):
        self.state = "CREATED"
        self.history = []


    def update(self, state):

        self.state = state

        self.history.append({
            "state": state,
            "timestamp": datetime.utcnow().isoformat()
        })


    def get(self):
        return {
            "current": self.state,
            "history": self.history
        }
