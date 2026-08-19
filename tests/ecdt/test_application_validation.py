import pytest

from intelligence.ecdt import (
    ApplicationEvidence,
    ApplicationValidation,
    ApplicationValidationGate,
    ValidationStatus,
)


def test_no_evidence_fails_closed():
    validator = ApplicationValidation()

    result = validator.validate("APP-001", [])

    assert result.status is ValidationStatus.INSUFFICIENT_EVIDENCE
    assert result.approved is False
    assert result.reasons == ("NO_EVIDENCE",)


def test_unverified_evidence_is_insufficient():
    validator = ApplicationValidation()

    evidence = [
        ApplicationEvidence(
            application_id="APP-001",
            source="wms",
            facts={"quantity": 12},
            verified=False,
        )
    ]

    result = validator.validate("APP-001", evidence)

    assert result.status is ValidationStatus.INSUFFICIENT_EVIDENCE
    assert result.verified_evidence_count == 0


def test_verified_evidence_can_be_approved():
    validator = ApplicationValidation()

    evidence = [
        ApplicationEvidence(
            application_id="APP-001",
            source="wms",
            facts={"quantity": 12},
            verified=True,
        )
    ]

    result = validator.validate("APP-001", evidence)

    assert result.status is ValidationStatus.APPROVED
    assert result.approved is True


def test_evidence_for_other_application_is_not_counted():
    validator = ApplicationValidation()

    evidence = [
        ApplicationEvidence(
            application_id="APP-OTHER",
            source="wms",
            verified=True,
        )
    ]

    result = validator.validate("APP-001", evidence)

    assert result.status is ValidationStatus.INSUFFICIENT_EVIDENCE
    assert result.evidence_count == 0


def test_configurable_verified_evidence_threshold():
    validator = ApplicationValidation(minimum_verified_evidence=2)

    evidence = [
        ApplicationEvidence(
            application_id="APP-001",
            source="wms",
            verified=True,
        )
    ]

    result = validator.validate("APP-001", evidence)

    assert result.status is ValidationStatus.INSUFFICIENT_EVIDENCE


def test_gate_allows_only_approved_result():
    gate = ApplicationValidationGate()

    evidence = [
        ApplicationEvidence(
            application_id="APP-001",
            source="digital-twin",
            verified=True,
        )
    ]

    assert gate.allows("APP-001", evidence) is True
    assert gate.allows("APP-002", evidence) is False


def test_empty_application_id_is_rejected():
    validator = ApplicationValidation()

    with pytest.raises(ValueError):
        validator.validate("", [])


def test_invalid_threshold_is_rejected():
    with pytest.raises(ValueError):
        ApplicationValidation(minimum_verified_evidence=0)
