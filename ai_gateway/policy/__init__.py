
from ai_gateway.policy.engine import PolicyEngine
from ai_gateway.policy.decision import PolicyDecision
from ai_gateway.policy.rules import PolicyRules


class PolicyGuard:

    def __init__(self):
        self.engine = PolicyEngine()

    def check(self, action):
        return self.engine.evaluate(action)

