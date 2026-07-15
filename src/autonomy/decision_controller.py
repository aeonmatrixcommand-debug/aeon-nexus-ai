from digital_twin.decision.decision_engine import DecisionEngine
from digital_twin.decision.simulation_engine import SimulationEngine
from digital_twin.governance.policy_engine import PolicyEngine


class DecisionController:
    """
    AEON MATRIX Autonomous Decision Controller.
    Sense -> Decide -> Simulate -> Govern
    """

    def __init__(self):
        self.decision_engine = DecisionEngine()
        self.simulation = SimulationEngine()
        self.policy = PolicyEngine()


    def evaluate(self, twin_state):

        twin_state = self.decision_engine.evaluate(
            twin_state
        )

        results = []

        for decision in twin_state.decisions:

            simulation = self.simulation.simulate(
                decision
            )

            governance = self.policy.check(
                decision["action"]
            )

            results.append({
                "decision": decision,
                "simulation": simulation,
                "governance": governance
            })

        return results
