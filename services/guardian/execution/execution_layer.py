from services.guardian.execution.action_executor import ActionExecutor
from services.guardian.execution.approval_gate import ApprovalGate
from services.guardian.execution.workflow_engine import WorkflowEngine
from services.guardian.execution.audit_trail import AuditTrail


class AutonomousExecutionLayer:

    def __init__(self):
        self.executor = ActionExecutor()
        self.approval = ApprovalGate()
        self.workflow = WorkflowEngine()
        self.audit = AuditTrail()

    def run(self, decision):

        approval = self.approval.approve(
            decision
        )

        if not approval["approved"]:
            return {
                "status": "WAITING_HUMAN_APPROVAL",
                "approval": approval
            }

        result = self.executor.execute(
            decision["action"]
        )

        return {
            "workflow": self.workflow.build(decision),
            "execution": result,
            "audit": self.audit.record(result)
        }
