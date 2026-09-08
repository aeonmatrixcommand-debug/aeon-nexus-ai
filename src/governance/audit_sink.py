"""Host-owned durable persistence contract. Providers never receive a sink.

Implementations acknowledge only committed appends, serialize concurrent writers,
verify recovery state, and reject same-key/different-event retries. The host must
vet a backend's actual guarantees; implementing this interface is not attestation.
"""

from abc import ABC, abstractmethod

from src.governance.audit_event import AuditReceipt


class DurableAuditSink(ABC):
    @abstractmethod
    def append(self, event: dict, *, idempotency_key: str) -> AuditReceipt:
        """Return a durable receipt after commit; never silently use memory."""

    @abstractmethod
    def history(self) -> list[dict]:
        """Read isolated snapshots after validating persisted chain integrity."""
