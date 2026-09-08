"""Host audit configuration. Production never falls back to process-local memory.

Set AEON_AUDIT_MODE=production and inject AuditTrail(SQLiteAudit(path),
mode='production') into both EvidenceGate and GovernedAnalysis. An explicit
audit_mode='production' on either boundary enforces the same rule. Development
is the backward-compatible default; hosts must deliberately select production.
Idempotency is for append retries, not exactly-once model inference.
"""

import os
import re
from uuid import uuid4

from src.governance.audit_event import AuditError, AuditReceipt
from src.governance.audit_sink import DurableAuditSink
from src.governance.immutable_audit import ImmutableAudit


class AuditTrail:

    def __init__(self, sink=None, *, mode=None):
        self.mode = audit_mode(mode)
        if self.mode == "production" and not isinstance(sink, DurableAuditSink):
            raise AuditError("durable_audit_required")
        self._sink = sink if sink is not None else ImmutableAudit()


    def record(self, event, *, idempotency_key=None):
        audit_mode(self.mode)
        durable = isinstance(self._sink, DurableAuditSink)
        if self.mode == "production" and not durable:
            raise AuditError("durable_audit_required")
        if durable:
            key = idempotency_key if idempotency_key is not None else event.get("request_id", uuid4().hex)
            receipt = self._sink.append(event, idempotency_key=key)
            if (not isinstance(receipt, AuditReceipt) or receipt.durable is not True
                    or type(receipt.audit_id) is not str
                    or not re.fullmatch("[0-9a-f]{32}", receipt.audit_id)
                    or type(receipt.sequence) is not int or receipt.sequence < 1
                    or type(receipt.digest) is not str
                    or not re.fullmatch("[0-9a-f]{64}", receipt.digest)
                    or type(receipt.previous_digest) is not str
                    or not re.fullmatch("[0-9a-f]{64}", receipt.previous_digest)):
                raise AuditError("durable_ack_required")
            return receipt
        if idempotency_key is not None:
            raise AuditError("idempotency_requires_durable_sink")
        return self._sink.append(event)


    def report(self):
        return self._sink.history()

    @property
    def logs(self):
        """Compatibility read access returns isolated snapshots."""
        return self.report()


def audit_mode(mode=None):
    configured = os.getenv("AEON_AUDIT_MODE", "development")
    resolved = configured if mode is None else mode
    if configured not in {"development", "production"} or resolved not in {"development", "production"}:
        raise AuditError("invalid_audit_mode")
    if configured == "production" and resolved != "production":
        raise AuditError("audit_mode_downgrade_denied")
    return resolved


def configured_audit(audit=None, *, mode=None):
    resolved = audit_mode(mode)
    if audit is None:
        return AuditTrail(mode=resolved)
    if resolved == "production" and not (
            isinstance(audit, AuditTrail) and audit.mode == "production"
            and isinstance(audit._sink, DurableAuditSink)):
        raise AuditError("durable_audit_required")
    return audit
