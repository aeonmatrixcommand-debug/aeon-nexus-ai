import pytest

from src.intelligence.ecdt.application_request import (
    ApplicationRequest,
)
from src.intelligence.ecdt.application_request_builder import (
    ApplicationRequestBuilder,
)


def proposal():
    return {
        "proposal_id": "proposal-001",
        "correlation_id": "corr-001",
        "status": "PROPOSED",
        "intended_change": {
            "target": "forecast_policy",
            "parameter": "safety_factor",
            "from": 1.0,
            "to": 1.1,
            "nested": {
                "source": "governed-learning",
            },
        },
    }


def authorization():
    return {
        "authorization_id": "auth-001",
        "proposal_id": "proposal-001",
        "status": "AUTHORIZED",
        "authorized_by": "human-reviewer",
    }


def test_build_application_request():
    result = ApplicationRequestBuilder().build(
        proposal=proposal(),
        authorization=authorization(),
    )

    assert isinstance(result, ApplicationRequest)
    assert result.status == "REQUESTED"
    assert result.proposal_id == "proposal-001"
    assert result.authorization_id == "auth-001"
    assert result.correlation_id == "corr-001"


def test_request_has_unique_identity():
    builder = ApplicationRequestBuilder()

    first = builder.build(
        proposal=proposal(),
        authorization=authorization(),
    )
    second = builder.build(
        proposal=proposal(),
        authorization=authorization(),
    )

    assert first.application_request_id
    assert second.application_request_id
    assert (
        first.application_request_id
        != second.application_request_id
    )


def test_rejects_non_authorized_status():
    auth = authorization()
    auth["status"] = "REJECTED"

    with pytest.raises(ValueError):
        ApplicationRequestBuilder().build(
            proposal=proposal(),
            authorization=auth,
        )


def test_rejects_mismatched_proposal_identity():
    auth = authorization()
    auth["proposal_id"] = "proposal-other"

    with pytest.raises(ValueError):
        ApplicationRequestBuilder().build(
            proposal=proposal(),
            authorization=auth,
        )


def test_requires_authorization_id():
    auth = authorization()
    auth["authorization_id"] = ""

    with pytest.raises(ValueError):
        ApplicationRequestBuilder().build(
            proposal=proposal(),
            authorization=auth,
        )


def test_requires_correlation_id():
    item = proposal()
    item["correlation_id"] = ""

    with pytest.raises(ValueError):
        ApplicationRequestBuilder().build(
            proposal=item,
            authorization=authorization(),
        )


def test_requires_intended_change():
    item = proposal()
    item.pop("intended_change")

    with pytest.raises(ValueError):
        ApplicationRequestBuilder().build(
            proposal=item,
            authorization=authorization(),
        )


def test_builder_does_not_mutate_inputs():
    item = proposal()
    auth = authorization()

    original_item = {
        **item,
        "intended_change": {
            **item["intended_change"],
            "nested": dict(
                item["intended_change"]["nested"]
            ),
        },
    }
    original_auth = dict(auth)

    ApplicationRequestBuilder().build(
        proposal=item,
        authorization=auth,
    )

    assert item == original_item
    assert auth == original_auth


def test_request_contains_defensive_change_snapshot():
    item = proposal()

    result = ApplicationRequestBuilder().build(
        proposal=item,
        authorization=authorization(),
    )

    item["intended_change"]["nested"]["source"] = "MUTATED"

    assert (
        result.intended_change["nested"]["source"]
        == "governed-learning"
    )


def test_to_dict_is_defensive():
    result = ApplicationRequestBuilder().build(
        proposal=proposal(),
        authorization=authorization(),
    )

    data = result.to_dict()
    data["intended_change"]["nested"]["source"] = "MUTATED"

    assert (
        result.to_dict()["intended_change"]["nested"]["source"]
        == "governed-learning"
    )


def test_builder_has_no_execution_interface():
    builder = ApplicationRequestBuilder()

    assert not hasattr(builder, "executor")
    assert not hasattr(builder, "execute")
    assert not hasattr(builder, "apply")
    assert not hasattr(builder, "deploy")
    assert not hasattr(builder, "promote")
    assert not hasattr(builder, "runtime")
    assert not hasattr(builder, "decision_memory")


def test_requested_does_not_imply_application():
    result = ApplicationRequestBuilder().build(
        proposal=proposal(),
        authorization=authorization(),
    ).to_dict()

    assert result["status"] == "REQUESTED"
    assert "executed" not in result
    assert "applied" not in result
    assert "deployed" not in result
    assert "promoted" not in result
