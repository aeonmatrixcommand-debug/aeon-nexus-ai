class ExplanationEngine:
    """
    Generate human understandable AI explanations.
    """

    def explain(self, decision, evidence):

        return {
            "decision": decision,
            "reason": self._build_reason(evidence),
            "evidence": evidence,
            "explainable": True
        }


    def _build_reason(self, evidence):

        if "temperature_deviation" in evidence:
            return (
                "Cold chain risk exceeded threshold "
                "because temperature deviation detected"
            )

        if "capacity_limit" in evidence:
            return (
                "Capacity shortage detected "
                "and operational risk increased"
            )

        return "Decision generated from simulation analysis"
