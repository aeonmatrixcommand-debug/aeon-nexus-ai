"""
AEON MATRIX AI Governance Audit Trail
Sprint 79
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class AuditEvent:
    decision: str
    source: str
    timestamp: str


class AuditTrail:
    """
    Records AI decision history.
    """

    def record(self, decision: str, source: str) -> AuditEvent:
        return AuditEvent(
            decision=decision,
            source=source,
            timestamp=datetime.utcnow().isoformat(),
        )
