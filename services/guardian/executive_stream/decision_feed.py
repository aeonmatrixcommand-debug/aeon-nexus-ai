from datetime import datetime


class ExecutiveDecisionFeed:

    def __init__(self):
        self.events = []

    def consume(self, event):
        record = {
            "module": event.get("module"),
            "decision": event.get("decision"),
            "confidence": event.get("confidence"),
            "risk_score": event.get("risk_score", 0),
            "status": "ACTIVE",
            "received_at": datetime.utcnow().isoformat(),
        }

        self.events.append(record)
        return record

    def latest(self):
        return self.events[-1] if self.events else None
