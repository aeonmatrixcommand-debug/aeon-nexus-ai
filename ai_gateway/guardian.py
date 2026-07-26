from datetime import datetime


class Guardian:

    def __init__(self):
        self.decisions = []


    def evaluate(
        self,
        risk
    ):

        if risk["risk_level"] == "CRITICAL":

            action = "IMMEDIATE_ISOLATION"


        elif risk["risk_level"] == "HIGH":

            action = "INVESTIGATION_REQUIRED"


        else:

            action = "MONITOR"


        decision = {
            "risk": risk,
            "action": action,
            "timestamp":
                datetime.utcnow().isoformat()
        }


        self.decisions.append(
            decision
        )


        return decision


    def history(self):

        return self.decisions
