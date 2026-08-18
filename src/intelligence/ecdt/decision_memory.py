"""Append-only decision memory for AEON MATRIX ECDT."""

from __future__ import annotations

from copy import deepcopy
from typing import Dict, List, Optional

from .decision_record import DecisionRecord


class DecisionMemory:
    """In-memory append-only store of immutable decision snapshots."""

    def __init__(self) -> None:
        self._records: List[Dict] = []
        self._decision_ids: set[str] = set()

    def append(self, record: DecisionRecord) -> str:
        snapshot = record.to_dict()
        decision_id = snapshot["decision_id"]

        if decision_id in self._decision_ids:
            raise ValueError(
                f"Decision already recorded: {decision_id}"
            )

        self._records.append(deepcopy(snapshot))
        self._decision_ids.add(decision_id)
        return decision_id

    def get(self, decision_id: str) -> Optional[Dict]:
        for record in self._records:
            if record["decision_id"] == decision_id:
                return deepcopy(record)
        return None

    def all(self) -> List[Dict]:
        return deepcopy(self._records)

    def __len__(self) -> int:
        return len(self._records)
