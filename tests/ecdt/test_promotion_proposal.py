from copy import deepcopy

import pytest

from src.intelligence.ecdt.promotion_proposal import (
    PromotionProposal,
)
from src.intelligence.ecdt.promotion_proposal_builder import (
    PromotionProposalBuilder,
)


def candidate():
    return {
        "candidate_id": "candidate-001",
        "source_decision_id": "decision-001",
        "correlation_id": "corr-001",
        "proposal": {
            "type": "capacity_adjustment",
        },
    }


def approval(status="APPROVED"):
    return {
        "approval_id": "approval-001",
        "candidate_id": "candidate-001",
        "status": status,
        "reason": "governance_criteria_satisfied",
    }


def intended_change():
    return {
        "target": "capacity_policy",
        "change": {
            "max_capacity": 120,
        },
    }


def test_approved_candidate_can_create_proposal():
    builder = PromotionProposalBuilder()

    result = builder.build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    )

    assert isinstance(result, PromotionProposal)
    assert result.status == "PROPOSED"
    assert result.candidate_id == "candidate-001"
    assert result.approval_id == "approval-001"


def test_rejected_approval_cannot_create_proposal():
    builder = PromotionProposalBuilder()

    with pytest.raises(ValueError):
        builder.build(
            candidate=candidate(),
            approval=approval("REJECTED"),
            intended_change=intended_change(),
        )


def test_human_review_required_cannot_create_proposal():
    builder = PromotionProposalBuilder()

    with pytest.raises(ValueError):
        builder.build(
            candidate=candidate(),
            approval=approval("HUMAN_REVIEW_REQUIRED"),
            intended_change=intended_change(),
        )


def test_candidate_identity_must_match_approval():
    builder = PromotionProposalBuilder()
    data = approval()
    data["candidate_id"] = "candidate-other"

    with pytest.raises(ValueError):
        builder.build(
            candidate=candidate(),
            approval=data,
            intended_change=intended_change(),
        )


def test_missing_candidate_id_is_invalid():
    builder = PromotionProposalBuilder()
    data = candidate()
    del data["candidate_id"]

    with pytest.raises(ValueError):
        builder.build(
            candidate=data,
            approval=approval(),
            intended_change=intended_change(),
        )


def test_missing_approval_id_is_invalid():
    builder = PromotionProposalBuilder()
    data = approval()
    del data["approval_id"]

    with pytest.raises(ValueError):
        builder.build(
            candidate=candidate(),
            approval=data,
            intended_change=intended_change(),
        )


def test_empty_intended_change_is_invalid():
    builder = PromotionProposalBuilder()

    with pytest.raises(ValueError):
        builder.build(
            candidate=candidate(),
            approval=approval(),
            intended_change={},
        )


def test_builder_does_not_mutate_inputs():
    builder = PromotionProposalBuilder()

    candidate_data = candidate()
    approval_data = approval()
    change_data = intended_change()

    original_candidate = deepcopy(candidate_data)
    original_approval = deepcopy(approval_data)
    original_change = deepcopy(change_data)

    builder.build(
        candidate=candidate_data,
        approval=approval_data,
        intended_change=change_data,
    )

    assert candidate_data == original_candidate
    assert approval_data == original_approval
    assert change_data == original_change


def test_serialized_proposal_is_defensive():
    builder = PromotionProposalBuilder()

    proposal = builder.build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    )

    result = proposal.to_dict()
    result["intended_change"]["change"]["max_capacity"] = 999
    result["evidence"]["candidate"]["candidate_id"] = "mutated"

    stored = proposal.to_dict()

    assert (
        stored["intended_change"]["change"]["max_capacity"]
        == 120
    )
    assert (
        stored["evidence"]["candidate"]["candidate_id"]
        == "candidate-001"
    )


def test_proposals_have_unique_identity():
    builder = PromotionProposalBuilder()

    first = builder.build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    )
    second = builder.build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    )

    assert first.proposal_id != second.proposal_id


def test_proposal_contains_correlation_identity():
    builder = PromotionProposalBuilder()

    result = builder.build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    )

    assert result.correlation_id == "corr-001"


def test_proposal_has_no_execution_authority():
    proposal = PromotionProposalBuilder().build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    )

    assert not hasattr(proposal, "executor")
    assert not hasattr(proposal, "execute")
    assert not hasattr(proposal, "deploy")
    assert not hasattr(proposal, "apply")
    assert not hasattr(proposal, "promote")


def test_builder_has_no_execution_or_runtime_interface():
    builder = PromotionProposalBuilder()

    assert not hasattr(builder, "executor")
    assert not hasattr(builder, "execute")
    assert not hasattr(builder, "deploy")
    assert not hasattr(builder, "apply")
    assert not hasattr(builder, "promote")
    assert not hasattr(builder, "runtime")
    assert not hasattr(builder, "decision_memory")


def test_proposed_does_not_imply_execution():
    result = PromotionProposalBuilder().build(
        candidate=candidate(),
        approval=approval(),
        intended_change=intended_change(),
    ).to_dict()

    assert result["status"] == "PROPOSED"
    assert "executed" not in result
    assert "deployed" not in result
    assert "applied" not in result
    assert "promoted" not in result
