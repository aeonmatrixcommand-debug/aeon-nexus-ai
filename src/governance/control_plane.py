from governance.policy_engine import PolicyEngine
from governance.approval_workflow import ApprovalWorkflow
from governance.audit_trail import AuditTrail
from governance.explainability import ExplainabilityEngine



class GovernanceControlPlane:


    def __init__(self):

        self.policy = PolicyEngine()

        self.approval = ApprovalWorkflow()

        self.audit = AuditTrail()

        self.explain = ExplainabilityEngine()



    def validate(self, action, reason):


        policy_result = self.policy.evaluate(
            action
        )


        if policy_result["approval_required"]:

            approval = self.approval.request(
                action,
                policy_result["risk_level"]
            )

        else:

            approval = {
                "status":"auto_approved"
            }


        explanation = self.explain.explain(
            action,
            reason
        )


        audit = self.audit.record(
            action
        )


        return {

            "policy":
            policy_result,

            "approval":
            approval,

            "explanation":
            explanation,

            "audit":
            audit

        }
