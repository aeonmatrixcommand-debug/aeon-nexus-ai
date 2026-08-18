"""Read-only replay of historical ECDT decisions.

DecisionReplay reconstructs a historical decision for inspection
without executing actions or creating new decision records.
"""

from copy import deepcopy
from typing import Any, Dict, Optional

from src.intelligence.ecdt.decision_memory import DecisionMemory
from src.intelligence.ecdt.decision_query import DecisionQuery


class DecisionReplay:
    """Safely reconstruct historical decisions without execution."""

    def __init__(self, memory: DecisionMemory) -> None:
        self._memory = memory
        self._query = DecisionQuery(memory)

    def replay(
        self,
        decision_id: str,
    ) -> Optional[Dict[str, Any]]:
        """Return a non-executable replay of a stored decision."""

        source = self._query.by_id(decision_id)

        if source is None:
            return None

        replay = {
            "replay": True,
            "executable": False,
            "source_decision_id": source["decision_id"],
            "correlation_id": source["correlation_id"],
            "timestamp": source["timestamp"],
            "proposed_action": source["proposed_action"],
            "evidence": deepcopy(source.get("evidence", [])),
            "reasoning": deepcopy(source.get("reasoning", {})),
            "simulation": deepcopy(source.get("simulation", {})),
            "policy": deepcopy(source.get("policy", {})),
            "approval": deepcopy(source.get("approval", {})),
            "execution": deepcopy(source.get("execution", {})),
            "verification": deepcopy(
                source.get("verification", {})
            ),
            "outcome": deepcopy(source.get("outcome", {})),
        }

        return replay
