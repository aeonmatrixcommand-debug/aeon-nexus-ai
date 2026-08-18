import pytest

from src.intelligence.ecdt.decision_memory import DecisionMemory
from src.intelligence.ecdt.decision_record import DecisionRecord


def sample_record():
    return DecisionRecord(
        proposed_action="optimize_capacity",
        evidence=[
            {
                "source": "WMS",
                "metric": "capacity",
                "value": 0.95,
            }
        ],
        reasoning={
            "risk_type": "capacity_shortage",
            "confidence": 0.86,
        },
        simulation={
            "scenario": "dynamic_labor_scaling",
            "status": "simulated",
        },
        policy={
            "allowed": True,
            "approval_required": False,
        },
    )


def test_decision_record_has_identity_and_timestamp():
    record = sample_record()

    assert record.decision_id
    assert record.correlation_id
    assert record.timestamp
    assert record.proposed_action == "optimize_capacity"


def test_decision_memory_appends_record():
    memory = DecisionMemory()
    record = sample_record()

    decision_id = memory.append(record)

    assert decision_id == record.decision_id
    assert len(memory) == 1
    assert memory.get(decision_id)["proposed_action"] == (
        "optimize_capacity"
    )


def test_duplicate_decision_cannot_be_appended():
    memory = DecisionMemory()
    record = sample_record()

    memory.append(record)

    with pytest.raises(ValueError):
        memory.append(record)


def test_returned_record_cannot_mutate_memory():
    memory = DecisionMemory()
    record = sample_record()
    memory.append(record)

    retrieved = memory.get(record.decision_id)
    retrieved["policy"]["allowed"] = False

    stored = memory.get(record.decision_id)

    assert stored["policy"]["allowed"] is True


def test_all_returns_defensive_copy():
    memory = DecisionMemory()
    record = sample_record()
    memory.append(record)

    records = memory.all()
    records.clear()

    assert len(memory) == 1
