"""
AEON MATRIX Decision Intelligence Engine
Human-in-the-loop Decision Layer
"""


class DecisionEngine:

    def __init__(self):
        self.name = "AEON MATRIX Decision Engine"


    def decide(self, kpi):

        risk = kpi.get("risk")

        if risk == "high":
            action = "escalate"
        elif risk == "medium":
            action = "monitor"
        else:
            action = "continue"

        return {
            "engine": self.name,
            "action": action,
            "risk": risk
        }


    def health(self):
        return {
            "status": "healthy",
            "engine": self.name
        }
