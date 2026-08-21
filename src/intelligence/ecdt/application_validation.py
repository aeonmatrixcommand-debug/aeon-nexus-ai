from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Tuple


@dataclass(frozen=True)
class ApplicationValidation:
    request_id: str
    status: str
    reasons: Tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "request_id": self.request_id,
            "status": self.status,
            "reasons": list(self.reasons),
        }
