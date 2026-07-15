from runtime.control_plane.action_registry import ActionRegistry
from runtime.control_plane.workflow_manager import WorkflowManager
from autonomy.execution_engine import ExecutionEngine


class AutonomyOrchestrator:
    """
    AEON MATRIX Autonomous Control Plane.
    """

    def __init__(self):

        self.registry = ActionRegistry()
        self.workflow = WorkflowManager()
        self.execution = ExecutionEngine()


    def run(self, action):

        workflow = self.workflow.start(action)

        metadata = self.registry.get(action)

        result = self.execution.execute(action)

        return {
            "workflow": workflow,
            "metadata": metadata,
            "execution": result
        }
