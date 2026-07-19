import json
import random
import time
from datetime import datetime


class TelemetryStream:


    def generate(self):

        temperature = round(
            random.uniform(45,75),2
        )

        workload = random.randint(
            30,95
        )

        latency = random.randint(
            20,150
        )

        agents = random.randint(
            5,25
        )


        health = 100

        if temperature > 65:
            health -= 10

        if latency > 100:
            health -= 5


        return {

            "system":
                "AEON MATRIX LIVE TELEMETRY",

            "timestamp":
                datetime.utcnow().isoformat(),


            "thermal":
                {
                    "ai_chip_temperature":
                        temperature,

                    "cooling":
                        "ACTIVE"
                },


            "compute":
                {
                    "workload":
                        workload,

                    "latency_ms":
                        latency
                },


            "agents":
                {
                    "active":
                        agents
                },


            "health":
                {
                    "score":
                        health,

                    "status":
                        (
                        "OPTIMAL"
                        if health >=90
                        else "WARNING"
                        )
                }
        }



if __name__ == "__main__":


    stream = TelemetryStream()


    print("="*70)
    print(" AEON MATRIX REAL-TIME TELEMETRY STREAM ")
    print("="*70)


    for i in range(5):

        print(
            json.dumps(
                stream.generate(),
                indent=2
            )
        )

        time.sleep(2)

