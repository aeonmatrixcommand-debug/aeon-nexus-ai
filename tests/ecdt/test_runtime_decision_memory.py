from src.intelligence.ecdt.decision_memory import DecisionMemory
from src.intelligence.ecdt.runtime import (
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


class FakeExecutor:
    def execute(self, action):
        return {
            "action": action,
            "status": "executed",
        }


def assert_recorded(runtime, result, expected_status):
    assert result["status"] == expected_status
    assert result["decision_recorded"] is True
    assert result["decision_id"]
    assert result["correlation_id"]

    assert len(runtime.decision_memory) == 1

    record = runtime.decision_memory.get(
        result["decision_id"]
    )

    assert record is not None
    assert record["decision_id"] == result["decision_id"]
    assert (
        record["correlation_id"]
        == result["correlation_id"]
    )
    assert record["proposed_action"] == result["action"]
    assert record["outcome"]["status"] == expected_status
    assert (
        record["outcome"]["executed"]
        == result["executed"]
    )


def test_dry_run_is_recorded():
    memory = DecisionMemory()
    runtime = ECDTRuntime(decision_memory=memory)

    result = runtime.run(**sample())

    assert_recorded(runtime, result, "DRY_RUN")


def test_human_required_is_recorded():
    memory = DecisionMemory()
    runtime = ECDTRuntime(decision_memory=memory)

    data = sample()
    data["action"] = "delete_inventory"

    result = runtime.run(**data)

    assert_recorded(runtime, result, "HUMAN_REQUIRED")


def test_blocked_decision_is_recorded():
    memory = DecisionMemory()
    runtime = ECDTRuntime(
        decision_memory=memory,
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    data = sample()
    data["action"] = "shutdown_system"

    result = runtime.run(
        **data,
        human_approved=True,
    )

    assert_recorded(runtime, result, "BLOCKED")


def test_executor_required_is_recorded():
    memory = DecisionMemory()
    runtime = ECDTRuntime(
        decision_memory=memory,
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    result = runtime.run(**sample())

    assert_recorded(
        runtime,
        result,
        "EXECUTOR_REQUIRED",
    )


def test_completed_execution_is_recorded():
    memory = DecisionMemory()
    runtime = ECDTRuntime(
        decision_memory=memory,
        executor=FakeExecutor(),
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    result = runtime.run(**sample())

    assert_recorded(runtime, result, "COMPLETED")

    record = memory.get(result["decision_id"])

    assert record["execution"]["status"] == "executed"
    assert record["verification"]["verified"] is True


def test_decisions_are_append_only_across_runs():
    memory = DecisionMemory()
    runtime = ECDTRuntime(decision_memory=memory)

    first = runtime.run(**sample())
    second = runtime.run(**sample())

    assert len(memory) == 2
    assert first["decision_id"] != second["decision_id"]
    assert first["correlation_id"] != second["correlation_id"]
