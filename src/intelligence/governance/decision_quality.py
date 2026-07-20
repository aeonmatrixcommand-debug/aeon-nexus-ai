"""
AEON MATRIX Decision Quality Intelligence
Sprint 82
"""


class DecisionQualityEngine:

    def score(
        self,
        confidence,
        outcome_success,
    ):

        return round(
            confidence * outcome_success,
            2,
        )
