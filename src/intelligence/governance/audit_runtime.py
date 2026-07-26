"""
AEON MATRIX Governance Audit Runtime
Sprint 81.1
"""

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class AuditRecord:
    action: str
    decision: str
    timestamp: str


class AuditRuntime:

    def record(
        self,
        action,
        decision,
    ):

        return AuditRecord(
            action=action,
            decision=decision,
            timestamp=datetime.now(UTC).isoformat(),
        )
