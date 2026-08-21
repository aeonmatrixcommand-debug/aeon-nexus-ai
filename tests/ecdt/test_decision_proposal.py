import pytest

from src.intelligence.ecdt import (
    DecisionProposal,
    DecisionProposalBuilder,
)


def recommendation():
    return {
        "name": "dynamic_labor_scaling",
        "action": "optimize_capacity",
    }


def evidence():
    return {
        "capacity": 0.95,
        "demand": 1.10,
        "source": "WMS",
    }


def test_proposal_is_created_as_proposed():
    proposal = DecisionProposalBuilder().build(
        recommendation=recommendation(),
        evidence=evidence(),
        policy_context={"allowed": True},
    )

    assert proposal.status == "PROPOSED"
    assert proposal.scenario_name == "dynamic_labor_scaling"
    assert proposal.action == "optimize_capacity"
    assert proposal.proposal_id.startswith("proposal-")


def test_proposal_serialization():
    proposal = DecisionProposalBuilder().build(
        recommendation=recommendation(),
        evidence=evidence(),
    )

    result = proposal.to_dict()

    assert result["status"] == "PROPOSED"
    assert result["scenario_name"] == "dynamic_labor_scaling"
    assert result["action"] == "optimize_capacity"
    assert result["proposal_id"].startswith("proposal-")
    assert result["evidence"]["source"] == "WMS"


def test_proposal_id_is_deterministic():
    builder = DecisionProposalBuilder()

    first = builder.build(
        recommendation=recommendation(),
        evidence=evidence(),
        policy_context={"allowed": True},
    )

    second = builder.build(
        recommendation=recommendation(),
        evidence=evidence(),
        policy_context={"allowed": True},
    )

    assert first.proposal_id == second.proposal_id


def test_policy_context_changes_proposal_identity():
    builder = DecisionProposalBuilder()

    allowed = builder.build(
        recommendation=recommendation(),
        evidence=evidence(),
        policy_context={"allowed": True},
    )

    blocked = builder.build(
        recommendation=recommendation(),
        evidence=evidence(),
        policy_context={"allowed": False},
    )

    assert allowed.proposal_id != blocked.proposal_id


def test_missing_recommendation_name_raises():
    data = recommendation()
    data["name"] = ""

    with pytest.raises(ValueError):
        DecisionProposalBuilder().build(
            recommendation=data,
            evidence=evidence(),
        )


def test_missing_action_raises():
    data = recommendation()
    data["action"] = ""

    with pytest.raises(ValueError):
        DecisionProposalBuilder().build(
            recommendation=data,
            evidence=evidence(),
        )


def test_missing_evidence_raises():
    with pytest.raises(ValueError):
        DecisionProposalBuilder().build(
            recommendation=recommendation(),
            evidence={},
        )


def test_proposal_has_no_execution_authority():
    proposal = DecisionProposalBuilder().build(
        recommendation=recommendation(),
        evidence=evidence(),
    )

    result = proposal.to_dict()

    for field in (
        "authorized",
        "authorization_id",
        "executed",
        "applied",
        "deployed",
        "promoted",
    ):
        assert field not in result


def test_builder_has_no_execution_interface():
    builder = DecisionProposalBuilder()

    for name in (
        "execute",
        "executor",
        "apply",
        "deploy",
        "promote",
        "authorize",
    ):
        assert not hasattr(builder, name)


def test_proposal_is_immutable():
    proposal = DecisionProposalBuilder().build(
        recommendation=recommendation(),
        evidence=evidence(),
    )

    with pytest.raises(Exception):
        proposal.status = "AUTHORIZED"
