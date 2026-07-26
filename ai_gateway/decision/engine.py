from ai_gateway.decision.confidence import ConfidenceEvaluator
from ai_gateway.decision.trace import DecisionTrace


class DecisionEngine:

    def __init__(self):
        self.confidence = ConfidenceEvaluator()
        self.trace = DecisionTrace()


    def analyze(self, action):

        score = self.confidence.evaluate(action)

        decision = "EXECUTE"

        if score < 0.7:
            decision = "REVIEW"

        result = {
            "decision": decision,
            "confidence": score
        }

        self.trace.record(
            action,
            decision,
            score
        )

        return result
