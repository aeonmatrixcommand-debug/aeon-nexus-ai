from digital_twin.autonomy.workflow_engine import WorkflowEngine


def test_workflow():

    result = WorkflowEngine().execute(
        [
            "analyze",
            "approve",
            "execute"
        ]
    )

    assert result["status"] == "executed"
