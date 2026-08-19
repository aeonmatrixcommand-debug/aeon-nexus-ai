"""Deterministic application validation primitives for AEON MATRIX ECDT."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class ValidationStatus(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


@dataclass(frozen=True)
class ApplicationEvidence:
    application_id: str
    source: str
    facts: Mapping[str, object] = field(default_factory=dict)
    verified: bool = False


@dataclass(frozen=True)
class ValidationResult:
    application_id: str
    status: ValidationStatus
    reasons: tuple[str, ...]
    evidence_count: int
    verified_evidence_count: int

    @property
    def approved(self) -> bool:
        return self.status is ValidationStatus.APPROVED


class ApplicationValidation:
    """Evaluates evidence without executing operational actions."""

    def __init__(self, minimum_verified_evidence: int = 1) -> None:
        if minimum_verified_evidence < 1:
            raise ValueError("minimum_verified_evidence must be >= 1")

        self.minimum_verified_evidence = minimum_verified_evidence

    def validate(
        self,
        application_id: str,
        evidence: list[ApplicationEvidence],
    ) -> ValidationResult:
        if not application_id.strip():
            raise ValueError("application_id must not be empty")

        relevant = tuple(
            item for item in evidence
            if item.application_id == application_id
        )

        if not relevant:
            return ValidationResult(
                application_id=application_id,
                status=ValidationStatus.INSUFFICIENT_EVIDENCE,
                reasons=("NO_EVIDENCE",),
                evidence_count=0,
                verified_evidence_count=0,
            )

        verified = tuple(item for item in relevant if item.verified)

        if len(verified) < self.minimum_verified_evidence:
            return ValidationResult(
                application_id=application_id,
                status=ValidationStatus.INSUFFICIENT_EVIDENCE,
                reasons=("VERIFIED_EVIDENCE_BELOW_THRESHOLD",),
                evidence_count=len(relevant),
                verified_evidence_count=len(verified),
            )

        if any(not item.source.strip() for item in verified):
            return ValidationResult(
                application_id=application_id,
                status=ValidationStatus.REJECTED,
                reasons=("INVALID_EVIDENCE_SOURCE",),
                evidence_count=len(relevant),
                verified_evidence_count=len(verified),
            )

        return ValidationResult(
            application_id=application_id,
            status=ValidationStatus.APPROVED,
            reasons=("EVIDENCE_THRESHOLD_SATISFIED",),
            evidence_count=len(relevant),
            verified_evidence_count=len(verified),
        )
