from datetime import datetime


class AutonomousAgent:

    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.status = "CREATED"
        self.history = []


    def transition(self, status):

        self.status = status

        self.history.append({
            "status": status,
            "timestamp": datetime.utcnow().isoformat()
        })


    def info(self):

        return {
            "agent_id": self.agent_id,
            "status": self.status,
            "history": self.history
        }
