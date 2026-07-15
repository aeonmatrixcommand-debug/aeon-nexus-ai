class ConfidenceOptimizer:
    """
    Improve decision confidence using experience.
    """

    def optimize(self, decision, experiences):

        base = 0.91

        if experiences:
            base += 0.04

        return {
            "decision": decision,
            "confidence": min(base, 0.99),
            "experience_used": len(experiences)
        }
