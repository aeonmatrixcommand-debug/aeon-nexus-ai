from services.guardian.execution.execution_engine import ExecutionEngine
from services.guardian.workflow.orchestrator import WorkflowOrchestrator
from services.guardian.execution.outcome_collector import OutcomeCollector


def test_autonomous_execution_flow():

    decision = {
        "decision": "INCREASE_ALLOCATION"
    }

    execution = ExecutionEngine().execute(decision)

    assert execution["status"] == "EXECUTED"

    workflow = WorkflowOrchestrator().run(execution)

    assert workflow["state"] == "COMPLETED"

    outcome = OutcomeCollector().collect(workflow)

    assert outcome["success"]
