class FeedbackEngine:
    """
    Learn from execution outcomes.
    """

    def evaluate(self, prediction, actual):

        difference = abs(
            prediction - actual
        )

        return {
            "prediction": prediction,
            "actual": actual,
            "error": difference,
            "learning_status": "captured"
        }
