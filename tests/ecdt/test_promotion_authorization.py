from dataclasses import FrozenInstanceError

import pytest

from src.intelligence.ecdt.promotion_authorization import (
    PromotionAuthorization,
)
from src.intelligence.ecdt.promotion_authorization_gate import (
    PromotionAuthorizationGate,
)


def proposal(
    *,
    status: str = "PROPOSED",
):
    return {
        "proposal_id": "proposal-1",
        "candidate_id": "candidate-1",
        "decision_id": "decision-1",
        "correlation_id": "corr-1",
        "status": status,
        "intended_change": {
            "parameter": "capacity_threshold",
            "from": 0.80,
            "to": 0.85,
        },
    }


def test_explicit_authorizer_can_authorize_proposal():
    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        authorized_by="human-reviewer",
        policy={"allowed": True},
    )

    data = result.to_dict()

    assert data["status"] == "AUTHORIZED"
    assert data["authorized_by"] == "human-reviewer"
    assert data["reason"] == "governance_authorized"


def test_missing_authorizer_requires_human():
    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        policy={"allowed": True},
    )

    assert result.to_dict()["status"] == "HUMAN_REQUIRED"


def test_policy_denial_rejects_proposal():
    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        authorized_by="human-reviewer",
        policy={"allowed": False},
    )

    data = result.to_dict()

    assert data["status"] == "REJECTED"
    assert data["reason"] == "policy_denied"


def test_non_proposed_input_is_rejected():
    result = PromotionAuthorizationGate().evaluate(
        proposal(status="DRAFT"),
        authorized_by="human-reviewer",
        policy={"allowed": True},
    )

    data = result.to_dict()

    assert data["status"] == "REJECTED"
    assert data["reason"] == "proposal_not_proposed"


def test_identity_chain_is_preserved():
    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        authorized_by="human-reviewer",
    ).to_dict()

    assert result["proposal_id"] == "proposal-1"
    assert result["candidate_id"] == "candidate-1"
    assert result["decision_id"] == "decision-1"
    assert result["correlation_id"] == "corr-1"


def test_scope_constraints_and_expiry_are_preserved():
    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        authorized_by="human-reviewer",
        policy={"allowed": True},
        scope={"environment": "staging"},
        constraints={"max_delta": 0.10},
        expires_at="2030-01-01T00:00:00+00:00",
    ).to_dict()

    assert result["scope"] == {
        "environment": "staging"
    }
    assert result["constraints"] == {
        "max_delta": 0.10
    }
    assert (
        result["expires_at"]
        == "2030-01-01T00:00:00+00:00"
    )


def test_authorization_has_unique_identity():
    gate = PromotionAuthorizationGate()

    first = gate.evaluate(
        proposal(),
        authorized_by="reviewer",
    )
    second = gate.evaluate(
        proposal(),
        authorized_by="reviewer",
    )

    assert (
        first.authorization_id
        != second.authorization_id
    )


def test_artifact_is_frozen():
    artifact = PromotionAuthorization(
        proposal_id="proposal-1",
        candidate_id="candidate-1",
        decision_id="decision-1",
        correlation_id="corr-1",
        status="AUTHORIZED",
        authorized_by="reviewer",
    )

    with pytest.raises(FrozenInstanceError):
        artifact.status = "REJECTED"


def test_to_dict_is_defensive():
    artifact = PromotionAuthorization(
        proposal_id="proposal-1",
        candidate_id="candidate-1",
        decision_id="decision-1",
        correlation_id="corr-1",
        status="AUTHORIZED",
        authorized_by="reviewer",
        policy={
            "allowed": True,
            "nested": {"source": "governance"},
        },
    )

    data = artifact.to_dict()
    data["policy"]["nested"]["source"] = "mutated"

    fresh = artifact.to_dict()

    assert (
        fresh["policy"]["nested"]["source"]
        == "governance"
    )


def test_input_mutation_does_not_change_authorization():
    source_policy = {
        "allowed": True,
        "nested": {"risk": "low"},
    }
    source_scope = {
        "environment": "staging",
    }

    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        authorized_by="reviewer",
        policy=source_policy,
        scope=source_scope,
    )

    source_policy["nested"]["risk"] = "critical"
    source_scope["environment"] = "production"

    data = result.to_dict()

    assert data["policy"]["nested"]["risk"] == "low"
    assert data["scope"]["environment"] == "staging"


def test_gate_has_no_execution_interface():
    gate = PromotionAuthorizationGate()

    assert not hasattr(gate, "executor")
    assert not hasattr(gate, "execute")
    assert not hasattr(gate, "apply")
    assert not hasattr(gate, "deploy")
    assert not hasattr(gate, "promote")


def test_gate_has_no_runtime_or_memory_interface():
    gate = PromotionAuthorizationGate()

    assert not hasattr(gate, "runtime")
    assert not hasattr(gate, "decision_memory")
    assert not hasattr(gate, "learning_engine")


def test_authorized_does_not_imply_application():
    result = PromotionAuthorizationGate().evaluate(
        proposal(),
        authorized_by="human-reviewer",
        policy={"allowed": True},
    ).to_dict()

    assert result["status"] == "AUTHORIZED"

    assert "executed" not in result
    assert "applied" not in result
    assert "deployed" not in result
    assert "promoted" not in result
