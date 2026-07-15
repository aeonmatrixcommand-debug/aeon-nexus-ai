from digital_twin.decision.decision_engine import DecisionEngine
from digital_twin.decision.simulation_engine import SimulationEngine
from digital_twin.decision.recommendation_engine import RecommendationEngine
from digital_twin.decision.confidence_engine import ConfidenceEngine


class DecisionRuntime:
    """
    Orchestrate Digital Twin decision intelligence flow.
    """

    def __init__(self):

        self.decision_engine = DecisionEngine()
        self.simulation_engine = SimulationEngine()
        self.recommendation_engine = RecommendationEngine()
        self.confidence_engine = ConfidenceEngine()


    def execute(self, twin_state):

        twin_state = self.decision_engine.evaluate(
            twin_state
        )

        simulations = []

        for decision in twin_state.decisions:

            result = self.simulation_engine.simulate(
                decision
            )

            simulations.append({
                **decision,
                **result
            })


        recommendation = (
            self.recommendation_engine.recommend(
                simulations
            )
        )


        confidence = (
            self.confidence_engine.calculate(
                recommendation
            )
        )


        twin_state.decision_result = {
            "recommendation": recommendation,
            "confidence": confidence
        }


        return twin_state
