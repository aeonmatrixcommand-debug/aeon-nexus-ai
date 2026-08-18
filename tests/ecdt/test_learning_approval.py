from copy import deepcopy

import pytest

from src.intelligence.ecdt.learning_approval import (
    LearningApproval,
    LearningApprovalStatus,
)
from src.intelligence.ecdt.learning_approval_gate import (
    LearningApprovalGate,
)


def candidate(
    *,
    eligible=True,
    human_review_required=False,
):
    return {
        "candidate_id": "candidate-001",
        "source_decision_id": "decision-001",
        "correlation_id": "corr-001",
        "eligible": eligible,
        "human_review_required": human_review_required,
        "proposal": {
            "type": "capacity_adjustment",
        },
    }


def test_ineligible_candidate_is_rejected():
    gate = LearningApprovalGate()

    result = gate.evaluate(candidate(eligible=False))

    assert result.status == LearningApprovalStatus.REJECTED
    assert result.reason == "candidate_not_eligible"


def test_human_review_cannot_be_inferred():
    gate = LearningApprovalGate()

    result = gate.evaluate(
        candidate(human_review_required=True)
    )

    assert (
        result.status
        == LearningApprovalStatus.HUMAN_REVIEW_REQUIRED
    )


def test_explicit_human_approval_can_approve():
    gate = LearningApprovalGate()

    result = gate.evaluate(
        candidate(human_review_required=True),
        human_approved=True,
    )

    assert result.status == LearningApprovalStatus.APPROVED
    assert result.reason == "human_approved"


def test_eligible_candidate_can_pass_governance():
    gate = LearningApprovalGate()

    result = gate.evaluate(candidate())

    assert result.status == LearningApprovalStatus.APPROVED


def test_missing_candidate_id_is_rejected_as_invalid():
    gate = LearningApprovalGate()
    data = candidate()
    del data["candidate_id"]

    with pytest.raises(ValueError):
        gate.evaluate(data)


def test_approval_has_unique_identity():
    gate = LearningApprovalGate()

    first = gate.evaluate(candidate())
    second = gate.evaluate(candidate())

    assert first.approval_id != second.approval_id


def test_approval_serialization_is_defensive():
    approval = LearningApproval(
        candidate_id="candidate-001",
        status=LearningApprovalStatus.APPROVED,
        reason="test",
        evidence={
            "nested": {
                "value": 1,
            }
        },
    )

    result = approval.to_dict()
    result["evidence"]["nested"]["value"] = 999

    stored = approval.to_dict()

    assert stored["evidence"]["nested"]["value"] == 1


def test_gate_does_not_mutate_candidate():
    gate = LearningApprovalGate()
    data = candidate()
    original = deepcopy(data)

    gate.evaluate(data)

    assert data == original


def test_gate_has_no_execution_interface():
    gate = LearningApprovalGate()

    assert not hasattr(gate, "executor")
    assert not hasattr(gate, "execute")
    assert not hasattr(gate, "deploy")
    assert not hasattr(gate, "promote")


def test_gate_has_no_runtime_or_learning_interface():
    gate = LearningApprovalGate()

    assert not hasattr(gate, "decision_memory")
    assert not hasattr(gate, "learning_engine")
    assert not hasattr(gate, "runtime")


def test_approval_is_not_a_promotion():
    result = LearningApprovalGate().evaluate(candidate())
    data = result.to_dict()

    assert data["status"] == "APPROVED"
    assert "deployed" not in data
    assert "promoted" not in data
    assert "executed" not in data
