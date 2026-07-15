from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class DecisionRequest:

    event: Dict[str, Any]
    decision: str



@dataclass
class DecisionResponse:

    result: Dict[str, Any]
    status: str
