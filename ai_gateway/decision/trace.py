from datetime import datetime


class DecisionTrace:

    def __init__(self):
        self.records = []


    def record(self, action, decision, confidence):

        self.records.append({
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "decision": decision,
            "confidence": confidence
        })


    def history(self):
        return self.records
