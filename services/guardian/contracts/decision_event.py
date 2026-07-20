from dataclasses import dataclass


@dataclass
class DecisionEvent:

    module: str
    decision: str
    confidence: float
    trace_id: str
