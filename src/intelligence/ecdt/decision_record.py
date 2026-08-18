"""Auditable decision records for AEON MATRIX ECDT."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List
from uuid import uuid4


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class DecisionRecord:
    """Immutable snapshot of one cognitive decision cycle."""

    proposed_action: str
    decision_id: str = field(default_factory=lambda: str(uuid4()))
    correlation_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: str = field(default_factory=_utc_now)

    evidence: List[Dict[str, Any]] = field(default_factory=list)
    reasoning: Dict[str, Any] = field(default_factory=dict)
    simulation: Dict[str, Any] = field(default_factory=dict)
    policy: Dict[str, Any] = field(default_factory=dict)
    approval: Dict[str, Any] = field(default_factory=dict)
    execution: Dict[str, Any] = field(default_factory=dict)
    verification: Dict[str, Any] = field(default_factory=dict)
    outcome: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return deepcopy(asdict(self))
