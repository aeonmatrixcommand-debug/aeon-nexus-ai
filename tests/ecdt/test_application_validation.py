from copy import deepcopy

import pytest

from src.intelligence.ecdt.application_validation import ApplicationValidation
from src.intelligence.ecdt.application_validation_gate import ApplicationValidationGate


def request():
    return {
        "request_id": "req-001",
        "proposal_id": "proposal-001",
        "authorization_id": "auth-001",
        "status": "REQUESTED",
        "intended_change": {
            "target": "forecast-policy",
            "change": "candidate-v2",
        },
    }


def test_validation_serialization():
    result = ApplicationValidation("req-001", "VALIDATED", ())
    assert result.to_dict() == {
        "request_id": "req-001",
        "status": "VALIDATED",
        "reasons": [],
    }


def test_valid_request_is_validated():
    result = ApplicationValidationGate().evaluate(
        request(), policy={"allowed": True}
    )
    assert result.status == "VALIDATED"
    assert result.reasons == ()


def test_non_requested_is_rejected():
    data = request()
    data["status"] = "AUTHORIZED"
    result = ApplicationValidationGate().evaluate(
        data, policy={"allowed": True}
    )
    assert result.status == "REJECTED"
    assert "REQUEST_NOT_REQUESTED" in result.reasons


def test_missing_authorization_is_rejected():
    data = request()
    data.pop("authorization_id")
    result = ApplicationValidationGate().evaluate(
        data, policy={"allowed": True}
    )
    assert "AUTHORIZATION_LINK_REQUIRED" in result.reasons


def test_missing_proposal_is_rejected():
    data = request()
    data.pop("proposal_id")
    result = ApplicationValidationGate().evaluate(
        data, policy={"allowed": True}
    )
    assert "PROPOSAL_LINK_REQUIRED" in result.reasons


def test_missing_change_is_rejected():
    data = request()
    data["intended_change"] = {}
    result = ApplicationValidationGate().evaluate(
        data, policy={"allowed": True}
    )
    assert "INTENDED_CHANGE_REQUIRED" in result.reasons


def test_disallowed_policy_is_rejected():
    result = ApplicationValidationGate().evaluate(
        request(), policy={"allowed": False}
    )
    assert result.status == "REJECTED"
    assert "POLICY_NOT_ALLOWED" in result.reasons


def test_none_request_raises():
    with pytest.raises(ValueError):
        ApplicationValidationGate().evaluate(None)


def test_missing_request_id_raises():
    data = request()
    data["request_id"] = ""
    with pytest.raises(ValueError):
        ApplicationValidationGate().evaluate(data)


def test_gate_does_not_mutate_request():
    data = request()
    original = deepcopy(data)
    ApplicationValidationGate().evaluate(
        data, policy={"allowed": True}
    )
    assert data == original


def test_gate_has_no_execution_interface():
    gate = ApplicationValidationGate()
    for name in ("executor", "execute", "apply", "deploy", "promote"):
        assert not hasattr(gate, name)


def test_gate_has_no_runtime_or_memory_interface():
    gate = ApplicationValidationGate()
    for name in ("runtime", "decision_memory", "learning_engine"):
        assert not hasattr(gate, name)


def test_validated_does_not_imply_application():
    result = ApplicationValidationGate().evaluate(
        request(), policy={"allowed": True}
    ).to_dict()

    assert result["status"] == "VALIDATED"

    for name in ("executed", "applied", "deployed", "promoted"):
        assert name not in result
