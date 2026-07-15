from simulation_engine.scenario_builder import ScenarioBuilder
from simulation_engine.impact_predictor import ImpactPredictor
from simulation_engine.what_if_engine import WhatIfEngine


class SimulationRuntime:

    def __init__(self):

        self.builder = ScenarioBuilder()
        self.predictor = ImpactPredictor()
        self.engine = WhatIfEngine()


    def simulate(self, decision):

        scenarios = self.builder.build(
            decision
        )

        impacts = []


        for scenario in scenarios:

            impact = self.predictor.predict(
                scenario
            )

            impacts.append(
                {
                    **scenario,
                    **impact
                }
            )


        return self.engine.compare(
            impacts
        )
