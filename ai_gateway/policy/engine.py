from ai_gateway.policy.rules import PolicyRules
from ai_gateway.policy.decision import PolicyDecision


class PolicyEngine:

    def __init__(self):
        self.rules = PolicyRules()

    def evaluate(self, action):

        result = self.rules.evaluate(action)

        return PolicyDecision(
            result["decision"],
            result["reason"],
            result["risk_score"]
        )
