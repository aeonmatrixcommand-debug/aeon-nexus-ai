import pytest

from src.intelligence.ecdt.authorization_request_builder import (
    AuthorizationRequestBuilder,
)
from src.intelligence.ecdt.application_validation_gate import (
    ApplicationValidationGate,
)


def proposal():
    return {
        "proposal_id": "proposal-001",
        "status": "PROPOSED",
        "action": "optimize_capacity",
        "evidence": {
            "source": "scenario-engine",
            "confidence": 0.91,
        },
    }


def test_builds_requested_authorization_request():
    request = AuthorizationRequestBuilder().build(
        proposal=proposal(),
    )

    result = request.to_dict()

    assert result["status"] == "REQUESTED"
    assert result["proposal_id"] == "proposal-001"
    assert result["request_id"].startswith("authreq-")
    assert result["intended_change"] == {
        "action": "optimize_capacity",
    }


def test_request_id_is_deterministic():
    builder = AuthorizationRequestBuilder()

    first = builder.build(proposal=proposal())
    second = builder.build(proposal=proposal())

    assert first.request_id == second.request_id


def test_request_contains_no_authorization_result():
    result = AuthorizationRequestBuilder().build(
        proposal=proposal(),
    ).to_dict()

    for field in (
        "authorization_id",
        "authorized",
        "human_approved",
        "executed",
        "applied",
        "deployed",
        "promoted",
    ):
        assert field not in result


def test_request_can_be_validated_without_prior_authorization():
    request = AuthorizationRequestBuilder().build(
        proposal=proposal(),
    )

    validation = ApplicationValidationGate().evaluate(
        request,
        policy={"allowed": True},
    )

    assert validation.status == "VALIDATED"
    assert validation.reasons == ()


def test_policy_can_reject_request():
    request = AuthorizationRequestBuilder().build(
        proposal=proposal(),
    )

    validation = ApplicationValidationGate().evaluate(
        request,
        policy={"allowed": False},
    )

    assert validation.status == "REJECTED"
    assert "POLICY_NOT_ALLOWED" in validation.reasons


def test_non_proposed_input_is_rejected():
    data = proposal()
    data["status"] = "AUTHORIZED"

    with pytest.raises(ValueError):
        AuthorizationRequestBuilder().build(
            proposal=data,
        )


def test_missing_proposal_id_is_rejected():
    data = proposal()
    data["proposal_id"] = ""

    with pytest.raises(ValueError):
        AuthorizationRequestBuilder().build(
            proposal=data,
        )


def test_builder_has_no_authority_interface():
    builder = AuthorizationRequestBuilder()

    for name in (
        "authorize",
        "approve",
        "execute",
        "executor",
        "apply",
        "deploy",
        "promote",
    ):
        assert not hasattr(builder, name)


def test_request_is_immutable():
    request = AuthorizationRequestBuilder().build(
        proposal=proposal(),
    )

    with pytest.raises(Exception):
        request.status = "AUTHORIZED"
