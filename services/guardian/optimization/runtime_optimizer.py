from services.guardian.optimization.decision_optimizer import DecisionOptimizer
from services.guardian.optimization.agent_ranker import AgentRanker


class RuntimeOptimizer:

    def __init__(self):
        self.decision = DecisionOptimizer()
        self.rank = AgentRanker()

    def optimize(self, event):

        return {
            "decision": self.decision.evaluate(event),
            "agents": self.rank.rank(
                event.get("agents", [])
            )
        }
