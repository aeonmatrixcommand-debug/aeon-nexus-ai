class PolicyDecision:

    def __init__(
        self,
        decision,
        reason,
        risk_score
    ):
        self.decision = decision
        self.reason = reason
        self.risk_score = risk_score

    def to_dict(self):
        return {
            "decision": self.decision,
            "reason": self.reason,
            "risk_score": self.risk_score
        }
