import json
from pathlib import Path
from datetime import datetime


class DigitalTwinSimulationEngine:

    def __init__(self, scenario_path):
        self.scenario_path = Path(scenario_path)
        self.scenario = self.load_scenario()

    def load_scenario(self):
        with open(self.scenario_path, "r") as file:
            return json.load(file)

    def analyze_telemetry(self):
        telemetry = self.scenario["telemetry"]

        risk = 0

        if telemetry["core_temperature_c"] > telemetry["temperature_threshold_c"]:
            risk += 40

        if telemetry["coolant_pressure_mpa"] < telemetry["optimal_pressure_mpa"]:
            risk += 35

        if telemetry["vibration_delta_percent"] > 200:
            risk += 15

        if telemetry["control_rod_insertion_percent"] < 20:
            risk += 10

        return {
            "risk_score": risk,
            "risk_level": (
                "CRITICAL"
                if risk >= 80
                else "HIGH"
                if risk >= 60
                else "NORMAL"
            )
        }

    def run_simulation(self):

        analysis = self.analyze_telemetry()

        result = {
            "simulation_id":
                f"DTS-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "scenario":
                self.scenario["scenario_id"],

            "system":
                self.scenario["system"],

            "analysis":
                analysis,

            "guardian":
                self.scenario["guardian_policy"],

            "actions":
                self.scenario["digital_twin_actions"],

            "status":
                "COMPLETED"
        }

        return result


if __name__ == "__main__":

    engine = DigitalTwinSimulationEngine(
        "digital_twin_safety/scenarios/FUSION_CORE_REACTOR_3_CRITICAL.json"
    )

    output = engine.run_simulation()

    print("=" * 40)
    print(" AEON MATRIX DIGITAL TWIN ENGINE")
    print("=" * 40)

    print(json.dumps(
        output,
        indent=2
    ))
