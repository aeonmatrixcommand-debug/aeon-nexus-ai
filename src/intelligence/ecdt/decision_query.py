"""Read-only query interface for ECDT decision memory."""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from src.intelligence.ecdt.decision_memory import DecisionMemory


class DecisionQuery:
    """Query historical decisions without mutating memory."""

    def __init__(self, memory: DecisionMemory) -> None:
        self._memory = memory

    def by_id(self, decision_id: str) -> Optional[Dict[str, Any]]:
        """Return one decision by its unique identifier."""
        return self._memory.get(decision_id)

    def by_correlation_id(
        self,
        correlation_id: str,
    ) -> List[Dict[str, Any]]:
        """Return decisions sharing a correlation identifier."""
        return self._filter("correlation_id", correlation_id)

    def by_action(
        self,
        action: str,
    ) -> List[Dict[str, Any]]:
        """Return decisions for a proposed action."""
        return self._filter("proposed_action", action)

    def by_status(
        self,
        status: str,
    ) -> List[Dict[str, Any]]:
        """Return decisions having the requested outcome status."""
        records = [
            record
            for record in self._memory.all()
            if record.get("outcome", {}).get("status") == status
        ]
        return deepcopy(records)

    def recent(
        self,
        limit: int = 10,
    ) -> List[Dict[str, Any]]:
        """Return the most recently appended decisions."""
        if limit < 0:
            raise ValueError("limit must be >= 0")

        if limit == 0:
            return []

        records = self._memory.all()
        return deepcopy(records[-limit:])

    def all(self) -> List[Dict[str, Any]]:
        """Return all decision records as defensive copies."""
        return deepcopy(self._memory.all())

    def _filter(
        self,
        field: str,
        value: Any,
    ) -> List[Dict[str, Any]]:
        records = [
            record
            for record in self._memory.all()
            if record.get(field) == value
        ]
        return deepcopy(records)
