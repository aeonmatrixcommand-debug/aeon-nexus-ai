from runtime.causal.causal_analyzer import CausalAnalyzer
from runtime.causal.impact_explainer import ImpactExplainer
from runtime.causal.decision_explainer import DecisionExplainer


class DecisionService:
    """
    Enterprise Decision Intelligence Service.
    """

    def __init__(self):

        self.causal = CausalAnalyzer()
        self.impact = ImpactExplainer()
        self.explainer = DecisionExplainer()


    def analyze(self, event, decision):

        causal_result = self.causal.analyze(
            event,
            decision
        )

        impact_result = self.impact.explain(
            decision
        )

        explanation = self.explainer.explain(
            decision,
            causal_result,
            impact_result
        )

        return {
            "event": event,
            "decision_intelligence": explanation,
            "status": "completed"
        }
