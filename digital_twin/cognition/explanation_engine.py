class ExplanationEngine:
    """
    Generate human understandable explanations.
    """

    def explain(self, event, reason, impact):

        return {
            "event": event,
            "reason": reason,
            "impact": impact,
            "explanation_status": "generated"
        }
