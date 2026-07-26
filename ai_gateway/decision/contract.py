from datetime import datetime


class DecisionContract:

    def __init__(
        self,
        decision,
        confidence,
        reason=None
    ):
        self.decision = decision
        self.confidence = confidence
        self.reason = reason
        self.timestamp = datetime.utcnow().isoformat()


    def to_dict(self):

        return {
            "decision": self.decision,
            "confidence": self.confidence,
            "reason": self.reason,
            "timestamp": self.timestamp
        }
