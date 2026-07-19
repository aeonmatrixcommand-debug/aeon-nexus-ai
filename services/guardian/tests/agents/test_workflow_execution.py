from services.guardian.agents.workflow.workflow_builder import build_workflow
from services.guardian.agents.workflow.execution_plan import create_plan


def test_workflow():

    workflow = build_workflow(
        "Demand Spike"
    )

    plan = create_plan(workflow)

    assert plan["status"] == "READY"
