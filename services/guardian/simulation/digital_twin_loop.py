from services.guardian.simulation.scenario_generator import ScenarioGenerator
from services.guardian.simulation.impact_engine import ImpactEngine


class DigitalTwinLoop:

    def __init__(self):
        self.generator = ScenarioGenerator()
        self.impact = ImpactEngine()

    def simulate(self, context):

        scenario = self.generator.create(
            context
        )

        result = self.impact.calculate(
            scenario
        )

        return {
            "scenario": scenario,
            "impact": result
        }
