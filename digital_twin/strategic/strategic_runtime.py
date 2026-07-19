from digital_twin.strategic.strategic_engine import StrategicEngine
from digital_twin.strategic.business_simulator import BusinessSimulator
from digital_twin.strategic.executive_engine import ExecutiveEngine


class StrategicRuntime:

    def __init__(self):

        self.strategy = StrategicEngine()
        self.simulator = BusinessSimulator()
        self.executive = ExecutiveEngine()


    def execute(self, insights):

        analysis = self.strategy.analyze(
            insights
        )

        decision = self.executive.decide(
            analysis
        )

        simulation = self.simulator.simulate(
            decision["decision"]
        )

        return {
            "analysis": analysis,
            "decision": decision,
            "simulation": simulation
        }
