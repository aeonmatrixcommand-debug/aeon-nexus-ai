from execution_fabric.execution_controller import ExecutionController
from execution_fabric.verification_engine import VerificationEngine


class AutonomousRuntime:

    def __init__(self):

        self.executor = ExecutionController()
        self.validator = VerificationEngine()


    def run(self, decision):

        execution = self.executor.execute(decision)

        verification = self.validator.verify(
            execution
        )

        return {
            "execution": execution,
            "verification": verification,
            "status": "autonomous_cycle_completed"
        }
