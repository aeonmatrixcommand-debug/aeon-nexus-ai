"""
AEON MATRIX Demand Shock Intelligence
Sprint 85
"""


class DemandShockDetector:

    def detect(
        self,
        forecast,
        actual,
    ):

        variance = abs(
            actual - forecast
        ) / forecast

        return {
            "variance": round(
                variance,
                2,
            ),
            "shock_detected": variance > 0.2,
        }
