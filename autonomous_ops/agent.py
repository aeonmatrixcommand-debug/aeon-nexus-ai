from mother_brain.decision import DecisionEngine


class AutonomousOperationsAgent:

    def __init__(self):
        self.decision = DecisionEngine()

    def process(self, event):

        if "inventory" in event.lower():
            action = "Inventory Re-Sync"

        elif "route" in event.lower():
            action = "Route Change Request"

        else:
            action = "Operational Review"

        decision = self.decision.process(action)

        return {
            "event": event,
            "action": action,
            "decision": decision
        }
