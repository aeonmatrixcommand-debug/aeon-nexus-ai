from guardian.policy_engine import PolicyEngine
from guardian.approval import ApprovalManager


class DecisionEngine:

    def __init__(self):
        self.policy = PolicyEngine()
        self.approval = ApprovalManager()

    def process(self, action):

        policy_result = self.policy.evaluate(action)

        execution = self.approval.request(
            policy_result
        )

        return {
            "policy": policy_result,
            "execution": execution
        }
