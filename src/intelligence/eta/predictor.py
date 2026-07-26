"""
AEON MATRIX ETA Prediction Intelligence
Sprint 85
"""


class ETAPredictor:

    def predict(
        self,
        distance,
        speed,
    ):

        return {
            "eta_hours": round(
                distance / speed,
                2,
            ),
            "confidence": 0.9,
        }
