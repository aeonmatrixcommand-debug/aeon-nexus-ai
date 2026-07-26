from datetime import datetime


class ActionEngine:

    def __init__(self):
        self.actions = []


    def create(self, decision):

        action = {
            "action": decision.get(
                "action",
                "NO_ACTION"
            ),
            "risk_level": decision.get(
                "risk",
                {}
            ).get(
                "risk_level",
                "UNKNOWN"
            ),
            "status": "PLANNED",
            "timestamp": datetime.utcnow().isoformat()
        }


        self.actions.append(action)

        return action


    def history(self):
        return self.actions
