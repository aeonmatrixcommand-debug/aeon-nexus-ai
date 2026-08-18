from src.intelligence.ecdt.decision_memory import DecisionMemory
from src.intelligence.ecdt.decision_record import DecisionRecord
from src.intelligence.ecdt.decision_replay import DecisionReplay


def sample_memory() -> tuple[DecisionMemory, DecisionRecord]:
    memory = DecisionMemory()

    record = DecisionRecord(
        proposed_action="optimize_capacity",
        correlation_id="corr-replay-1",
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
        execution={
            "status": "executed",
        },
        verification={
            "verified": True,
        },
        outcome={
            "status": "COMPLETED",
            "executed": True,
            "execution_mode": "EXECUTE",
        },
    )

    memory.append(record)
    return memory, record


def test_replay_existing_decision():
    memory, record = sample_memory()
    replay = DecisionReplay(memory)

    result = replay.replay(record.decision_id)

    assert result is not None
    assert result["replay"] is True
    assert result["executable"] is False
    assert result["source_decision_id"] == record.decision_id
    assert result["proposed_action"] == "optimize_capacity"


def test_unknown_decision_returns_none():
    memory, _ = sample_memory()
    replay = DecisionReplay(memory)

    assert replay.replay("missing-decision") is None


def test_replay_preserves_correlation_identity():
    memory, record = sample_memory()
    replay = DecisionReplay(memory)

    result = replay.replay(record.decision_id)

    assert result is not None
    assert result["source_decision_id"] == record.decision_id
    assert result["correlation_id"] == record.correlation_id


def test_replay_does_not_append_memory():
    memory, record = sample_memory()
    replay = DecisionReplay(memory)

    before = len(memory)

    replay.replay(record.decision_id)

    assert len(memory) == before


def test_replay_result_cannot_mutate_memory():
    memory, record = sample_memory()
    replay = DecisionReplay(memory)

    result = replay.replay(record.decision_id)

    assert result is not None

    result["policy"]["allowed"] = False
    result["outcome"]["status"] = "MUTATED"

    stored = memory.get(record.decision_id)

    assert stored is not None
    assert stored["policy"]["allowed"] is True
    assert stored["outcome"]["status"] == "COMPLETED"


def test_replay_has_no_executor_interface():
    memory, _ = sample_memory()
    replay = DecisionReplay(memory)

    assert not hasattr(replay, "executor")
    assert not hasattr(replay, "execute")
