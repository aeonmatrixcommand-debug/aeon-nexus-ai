from src.intelligence.ecdt import (
    ECDTExecutionMode,
    ECDTRuntime,
)


def sample():
    return {
        "signals": [
            {
                "source": "WMS",
                "metric": "capacity",
                "value": 0.95,
            }
        ],
        "risk": {
            "type": "capacity_shortage",
        },
        "scenario": {
            "name": "dynamic_labor_scaling",
        },
        "action": "optimize_capacity",
    }


def test_ecdt_defaults_to_dry_run():
    runtime = ECDTRuntime()

    result = runtime.run(**sample())

    assert result["status"] == "DRY_RUN"
    assert result["executed"] is False
    assert result["sense"]["signal_count"] == 1
    assert result["simulate"]["status"] == "simulated"


def test_execution_requires_explicit_executor():
    runtime = ECDTRuntime(
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    result = runtime.run(**sample())

    assert result["status"] == "EXECUTOR_REQUIRED"
    assert result["executed"] is False


def test_execution_guard_cannot_be_bypassed():
    runtime = ECDTRuntime(
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    data = sample()
    data["action"] = "shutdown_system"

    result = runtime.run(
        **data,
        human_approved=True,
    )

    assert result["status"] == "BLOCKED"
    assert result["executed"] is False


def test_restricted_action_requires_human():
    runtime = ECDTRuntime()

    data = sample()
    data["action"] = "delete_inventory"

    result = runtime.run(**data)

    assert result["status"] == "HUMAN_REQUIRED"
    assert result["executed"] is False
    assert result["governance"]["approval"]["human_required"] is True


class FakeExecutor:
    def execute(self, action):
        return {
            "action": action,
            "status": "executed",
        }


def test_explicit_execution_path():
    runtime = ECDTRuntime(
        executor=FakeExecutor(),
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    result = runtime.run(**sample())

    assert result["status"] == "COMPLETED"
    assert result["executed"] is True
    assert result["verification"]["verified"] is True
    assert result["learning"]["learning_status"] == "active"
