import pytest

from src.intelligence.ecdt.decision_memory import DecisionMemory
from src.intelligence.ecdt.decision_query import DecisionQuery
from src.intelligence.ecdt.decision_record import DecisionRecord


def record(
    action: str,
    status: str,
    correlation_id: str,
) -> DecisionRecord:
    return DecisionRecord(
        proposed_action=action,
        correlation_id=correlation_id,
        outcome={
            "status": status,
            "executed": False,
        },
    )


def memory_with_records() -> DecisionMemory:
    memory = DecisionMemory()

    memory.append(
        record(
            "optimize_capacity",
            "DRY_RUN",
            "corr-1",
        )
    )
    memory.append(
        record(
            "delete_inventory",
            "HUMAN_REQUIRED",
            "corr-2",
        )
    )
    memory.append(
        record(
            "optimize_capacity",
            "COMPLETED",
            "corr-1",
        )
    )

    return memory


def test_query_by_id():
    memory = memory_with_records()
    query = DecisionQuery(memory)

    decision_id = memory.all()[0]["decision_id"]

    result = query.by_id(decision_id)

    assert result is not None
    assert result["decision_id"] == decision_id


def test_query_by_correlation_id():
    query = DecisionQuery(memory_with_records())

    results = query.by_correlation_id("corr-1")

    assert len(results) == 2


def test_query_by_action():
    query = DecisionQuery(memory_with_records())

    results = query.by_action("optimize_capacity")

    assert len(results) == 2
    assert all(
        item["proposed_action"] == "optimize_capacity"
        for item in results
    )


def test_query_by_status():
    query = DecisionQuery(memory_with_records())

    results = query.by_status("HUMAN_REQUIRED")

    assert len(results) == 1
    assert (
        results[0]["proposed_action"]
        == "delete_inventory"
    )


def test_recent():
    query = DecisionQuery(memory_with_records())

    results = query.recent(2)

    assert len(results) == 2
    assert results[-1]["outcome"]["status"] == "COMPLETED"


def test_recent_zero():
    query = DecisionQuery(memory_with_records())

    assert query.recent(0) == []


def test_recent_rejects_negative_limit():
    query = DecisionQuery(memory_with_records())

    with pytest.raises(ValueError):
        query.recent(-1)


def test_query_results_cannot_mutate_memory():
    memory = memory_with_records()
    query = DecisionQuery(memory)

    results = query.by_status("DRY_RUN")
    results[0]["outcome"]["status"] = "MUTATED"

    stored = query.by_status("DRY_RUN")

    assert len(stored) == 1
    assert stored[0]["outcome"]["status"] == "DRY_RUN"


def test_all_is_defensive():
    memory = memory_with_records()
    query = DecisionQuery(memory)

    results = query.all()
    results.clear()

    assert len(query.all()) == 3
