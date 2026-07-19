from dataclasses import dataclass


@dataclass
class LearningEvent:

    source: str
    pattern: str
    improvement: float
    confidence: float
