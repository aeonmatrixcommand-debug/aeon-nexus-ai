class ConfidenceCalibrator:
    """
    Adjust AI confidence based on historical accuracy.
    """

    def calibrate(self, confidence, accuracy):

        adjusted = confidence * accuracy

        return {
            "original_confidence": confidence,
            "accuracy": accuracy,
            "adjusted_confidence": round(adjusted, 2),
            "status": "calibrated"
        }
