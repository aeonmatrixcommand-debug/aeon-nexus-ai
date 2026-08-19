from services.guardian.execution.action_executor import ActionExecutor
from services.guardian.execution.workflow_engine import WorkflowEngine
from services.guardian.execution.audit_trail import AuditTrail
from services.guardian.execution.authorization import AuthorizationIssuer
from services.guardian.execution.authorization_consumption import AuthorizationConsumptionRegistry
from services.guardian.governance.policy_engine import PolicyEngine
from services.guardian.governance.approval_gate import ApprovalGate


class AutonomousExecutionLayer:
    """
    Fail-closed execution boundary.

    Execution requires all of the following:

      1. Guardian policy approval.
      2. Guardian approval gate approval.
      3. A valid Guardian-issued ExecutionAuthorization.
      4. Authority bound to the exact decision and action.

    Confidence is evidence, not execution authority.
    Boolean authorization flags are not trusted.
    """

    def __init__(self, authorization_consumption=None):
        self.executor = ActionExecutor()
        self.policy = PolicyEngine()
        self.approval = ApprovalGate()
        self.authority = AuthorizationIssuer()
        self.authorization_consumption = (
            authorization_consumption
            if authorization_consumption is not None
            else AuthorizationConsumptionRegistry()
        )
        self.workflow = WorkflowEngine()
        self.audit = AuditTrail()

    def run(self, decision):
        policy = self.policy.evaluate(decision)
        approval = self.approval.request(policy)

        if not approval["approved"]:
            return {
                "status": (
                    "WAITING_HUMAN_APPROVAL"
                    if approval["human_required"]
                    else "BLOCKED"
                ),
                "policy": policy,
                "approval": approval,
            }

        decision_id = decision.get("decision_id")
        action = decision.get("action")
        execution_authority = decision.get("execution_authority")

        if not decision_id:
            return {
                "status": "BLOCKED",
                "reason": "DECISION_ID_REQUIRED",
                "policy": policy,
                "approval": approval,
            }

        if not action:
            return {
                "status": "BLOCKED",
                "reason": "ACTION_REQUIRED",
                "policy": policy,
                "approval": approval,
            }

        if not self.authority.verify(
            execution_authority,
            decision_id=decision_id,
            action=action,
        ):
            return {
                "status": "BLOCKED",
                "reason": "EXECUTION_AUTHORIZATION_REQUIRED",
                "policy": policy,
                "approval": approval,
            }

        if not self.authorization_consumption.try_consume(
            execution_authority.authorization_id
        ):
            return {
                "status": "BLOCKED",
                "reason": "EXECUTION_AUTHORITY_ALREADY_CONSUMED",
                "policy": policy,
                "approval": approval,
            }

        result = self.executor.execute(action)

        return {
            "status": "EXECUTED",
            "policy": policy,
            "approval": approval,
            "authorization": {
                "authorization_id": execution_authority.authorization_id,
                "issued_by": execution_authority.issued_by,
                "decision_id": execution_authority.decision_id,
                "action": execution_authority.action,
            },
            "workflow": self.workflow.build(decision),
            "execution": result,
            "audit": self.audit.record(result),
        }
