"""
AEON MATRIX Digital Twin Confidence Intelligence
Sprint 79.8
"""


class ConfidenceIndexEngine:
    """
    Calculates reliability score of digital twin state.
    """

    def calculate(
        self,
        freshness: float,
        accuracy: float,
        completeness: float,
    ) -> float:
        return round(
            (freshness + accuracy + completeness) / 3,
            2,
        )
