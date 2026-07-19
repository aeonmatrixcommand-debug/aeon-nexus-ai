import json
import random
from datetime import datetime


class NeuralReactor:


    def generate(self):

        temperature = round(
            random.uniform(45,80),2
        )

        workload = random.randint(
            30,100
        )

        vibration = random.randint(
            0,50
        )

        health = 100


        if temperature > 70:
            health -= 10

        if workload > 90:
            health -= 8


        if health >=90:
            state = "OPTIMAL"

        elif health >=70:
            state = "WARNING"

        else:
            state = "CRITICAL"


        return {

            "visualization":
                "AEON MATRIX NEURAL REACTOR",

            "timestamp":
                datetime.utcnow().isoformat(),


            "core_animation":
                {
                    "pulse":
                        "ACTIVE",

                    "rotation":
                        random.randint(0,360),

                    "energy_level":
                        workload
                },


            "thermal_heat_map":
                {
                    "temperature_c":
                        temperature,

                    "zone":
                        (
                        "GREEN"
                        if temperature <60
                        else "YELLOW"
                        if temperature <75
                        else "RED"
                        )
                },


            "ai_health_ring":
                {
                    "score":
                        health,

                    "state":
                        state
                },


            "digital_twin":
                {
                    "simulation":
                        "RUNNING",

                    "confidence":
                        random.randint(90,99)
                },


            "alerts":
                (
                []
                if state=="OPTIMAL"
                else
                [
                    "HIGH COMPUTE LOAD",
                    "THERMAL MONITORING REQUIRED"
                ]
                )
        }



if __name__ == "__main__":


    engine = NeuralReactor()


    print("="*70)
    print(" AEON MATRIX ADVANCED VISUALIZATION ENGINE ")
    print("="*70)


    print(
        json.dumps(
            engine.generate(),
            indent=2
        )
    )

