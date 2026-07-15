from digital_twin.governance.execution_guard import ExecutionGuard


def test_execution_guard():

    result = ExecutionGuard().validate(
        "optimize_route"
    )

    assert result["allowed"] is True
