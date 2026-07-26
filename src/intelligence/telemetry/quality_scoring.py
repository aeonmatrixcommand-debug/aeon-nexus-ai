"""
AEON MATRIX Telemetry Quality Intelligence
Sprint 79
"""


class TelemetryQualityScorer:
    """
    Evaluates operational signal quality.
    """

    def score(self, freshness: float, accuracy: float) -> float:
        return round(
            (freshness + accuracy) / 2,
            2
        )
