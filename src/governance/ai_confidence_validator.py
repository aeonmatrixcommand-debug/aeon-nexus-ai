class AIConfidenceValidator:
    def is_trusted(self, confidence: float):
        return confidence >= 0.85
