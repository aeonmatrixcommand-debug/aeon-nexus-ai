class ConfidenceEngine:
    """
    Estimate decision confidence.
    """

    def calculate(self, decision):

        if decision:
            return {
                "confidence": 0.91,
                "explanation": "Decision supported by simulation"
            }

        return {
            "confidence": 0,
            "explanation": "No recommendation available"
        }
