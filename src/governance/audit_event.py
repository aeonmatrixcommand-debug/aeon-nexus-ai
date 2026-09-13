"""Versioned metadata-only durable audit records and canonical serialization.

No free-form fields are persisted. Unknown fields are discarded; recognized
fields accept only fixed vocabulary, opaque IDs, booleans, and digests. This is
an allowlist, not a claim that arbitrary secret text can be reliably redacted.
"""

from dataclasses import dataclass
import hashlib
import json
import re


GENESIS_DIGEST = "0" * 64


class AuditError(RuntimeError):
    """Sanitized audit failure; never include caller payload or storage errors."""


class AuditIntegrityError(AuditError):
    pass


class IdempotencyConflict(AuditError):
    pass


def canonical_json(value) -> str:
    """Version 1 canonical encoding (Python JSON, ASCII, sorted, finite)."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False)


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class AuditReceipt:
    audit_id: str
    sequence: int
    digest: str
    previous_digest: str = GENESIS_DIGEST
    durable: bool = False
    duplicate: bool = False


VOCABULARY = {
    "event_type": {"EVIDENCE_COLLECTION_FAILED", "ADVISORY_DECISION"},
    "stage": {"evidence_collection", "capability_egress", "evidence", "pre_governance",
              "provider", "output_validation", "post_guardian", "release"},
    "reason": {"invalid_evidence", "egress_denied", "invalid_request", "capability_denied",
               "physical_execution_denied", "tms_read_only_required", "governance_denied",
               "provider_failed", "invalid_output", "guardian_denied", "boundary_failed",
               "validated", "audit_unavailable"},
    "status": {"NO_DECISION", "PROPOSED"},
    "mode": {"SIMULATION_ONLY", "READ_ONLY"},
}


@dataclass(frozen=True)
class AuditEvent:
    """Immutable serialized snapshot. Build using from_mapping()."""
    canonical: str

    @classmethod
    def from_mapping(cls, event: dict):
        try:
            if type(event) is not dict:
                raise ValueError()
            clean = {}
            for key, allowed in VOCABULARY.items():
                if key in event:
                    if type(event[key]) is not str or event[key] not in allowed:
                        raise ValueError()
                    clean[key] = event[key]
            for key in ("execution_authorized", "executed"):
                if event.get(key) is not False:
                    raise ValueError()
                clean[key] = False
            for key, length in (("request_id", 32), ("output_digest", 64)):
                if key in event:
                    if type(event[key]) is not str or not re.fullmatch(
                            "[0-9a-f]{%d}" % length, event[key]):
                        raise ValueError()
                    clean[key] = event[key]
            if "evidence_ids" in event:
                refs = event["evidence_ids"]
                if (type(refs) is not list or len(refs) > 100
                        or any(type(ref) is not str or not re.fullmatch("[0-9a-f]{32}", ref)
                               for ref in refs) or len(set(refs)) != len(refs)):
                    raise ValueError()
                clean["evidence_ids"] = list(refs)
            if not {"stage", "reason", "status"} <= clean.keys():
                raise ValueError()
            if clean["status"] == "PROPOSED" and not (
                    clean["stage"] == "release" and clean["reason"] == "validated"
                    and clean.get("evidence_ids") and "output_digest" in clean
                    and "request_id" in clean and "mode" in clean):
                raise ValueError()
            return cls(canonical_json(clean))
        except Exception:
            raise AuditError("invalid_audit_event") from None

    def to_dict(self):
        return json.loads(self.canonical)
