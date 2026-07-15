class DecisionExplainer:
    """
    Generate explainable AI decision.
    """

    def explain(
        self,
        decision,
        causal,
        impact
    ):

        return {

            "decision": decision,

            "reason": causal["causes"],

            "causal_chain":
                causal["causal_chain"],

            "impact": impact,

            "confidence": 0.95,

            "explainability":
                "complete"

        }
