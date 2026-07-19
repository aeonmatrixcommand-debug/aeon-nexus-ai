import json
import random
from datetime import datetime


class NeuralCore:

    def telemetry(self):

        temperature = round(
            random.uniform(45,70),2
        )

        workload = random.randint(
            40,95
        )

        agents = random.randint(
            4,20
        )

        health = 100

        if temperature > 65:
            health -= 8

        if workload > 85:
            health -= 5


        return {

            "core":
                "AEON MATRIX NEURAL CORE",

            "timestamp":
                datetime.utcnow().isoformat(),

            "thermal":
                {
                    "ai_temperature_c":
                        temperature,

                    "cooling":
                        "ACTIVE"
                },

            "compute":
                {
                    "workload_percent":
                        workload,

                    "processing_mode":
                        "REAL_TIME"
                },

            "agents":
                {
                    "active_agents":
                        agents,

                    "status":
                        "COORDINATED"
                },

            "intelligence_health":
                {
                    "score":
                        health,

                    "state":
                        (
                        "OPTIMAL"
                        if health >=90
                        else "WARNING"
                        )
                },

            "neural_state":
                "EVOLVING"
        }


if __name__ == "__main__":

    core = NeuralCore()

    print("="*70)
    print(" AEON MATRIX NEURAL COMMAND CORE ")
    print("="*70)

    print(json.dumps(
        core.telemetry(),
        indent=2
    ))
