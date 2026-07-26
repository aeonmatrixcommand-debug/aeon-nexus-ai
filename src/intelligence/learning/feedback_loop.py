"""
AEON MATRIX Autonomous Learning Feedback Loop
Sprint 80
"""

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class FeedbackResult:
    action_id: str
    outcome: str
    improvement_score: float
    timestamp: str


class FeedbackLoop:

    def evaluate(
        self,
        action_id: str,
        outcome: str,
        improvement_score: float,
    ) -> FeedbackResult:

        return FeedbackResult(
            action_id=action_id,
            outcome=outcome,
            improvement_score=improvement_score,
            timestamp=datetime.now(UTC).isoformat(),
        )
