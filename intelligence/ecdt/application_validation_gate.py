"""Decision gate for ECDT application validation."""

from __future__ import annotations

from .application_validation import (
    ApplicationEvidence,
    ApplicationValidation,
    ValidationResult,
)


class ApplicationValidationGate:
    """
    Fail-closed gate.

    The gate validates evidence only. It does not execute the requested
    business action and therefore preserves separation between intelligence,
    governance, and operational execution.
    """

    def __init__(self, validator: ApplicationValidation | None = None) -> None:
        self.validator = validator or ApplicationValidation()

    def evaluate(
        self,
        application_id: str,
        evidence: list[ApplicationEvidence],
    ) -> ValidationResult:
        return self.validator.validate(application_id, evidence)

    def allows(
        self,
        application_id: str,
        evidence: list[ApplicationEvidence],
    ) -> bool:
        return self.evaluate(application_id, evidence).approved
