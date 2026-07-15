from digital_twin.governance.policy_engine import PolicyEngine
from digital_twin.governance.approval_engine import ApprovalEngine
from digital_twin.governance.action_engine import ActionEngine
from digital_twin.governance.audit_engine import AuditEngine


class GovernanceRuntime:

    def __init__(self):

        self.policy = PolicyEngine()
        self.approval = ApprovalEngine()
        self.action = ActionEngine()
        self.audit = AuditEngine()


    def execute(self, action):

        policy = self.policy.check(action)

        if not policy["allowed"]:

            approval = self.approval.request(action)

            return {
                "policy": policy,
                "approval": approval
            }


        result = self.action.execute(action)

        audit = self.audit.record(
            action,
            result
        )

        return {
            "policy": policy,
            "result": result,
            "audit": audit
        }
