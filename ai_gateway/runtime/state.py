from datetime import datetime


class RuntimeState:

    def __init__(self):
        self.state = {
            "status": "IDLE",
            "action": None,
            "history": []
        }


    def update(self, status, action=None):

        record = {
            "status": status,
            "action": action,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.state["status"] = status
        self.state["action"] = action
        self.state["history"].append(record)

        return record


    def current(self):
        return self.state
