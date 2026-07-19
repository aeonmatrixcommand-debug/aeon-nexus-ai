import json
import time
import random
from datetime import datetime


def generate_signal():

    temperature = round(
        random.uniform(45,75),2
    )

    workload = random.randint(
        30,95
    )

    health = max(
        0,
        100 -
        int((temperature-45)/3)
    )


    return {
        "timestamp":
            datetime.utcnow().isoformat(),

        "thermal":
            {
                "temperature":
                    temperature
            },

        "compute":
            {
                "workload":
                    workload
            },

        "agents":
            {
                "active":
                    random.randint(5,20)
            },

        "core_state":
            (
            "OPTIMAL"
            if health >=90
            else "WARNING"
            ),

        "health":
            health
    }


if __name__ == "__main__":

    print(
        "AEON MATRIX WEBSOCKET TELEMETRY GATEWAY"
    )

    for _ in range(5):

        print(
            json.dumps(
                generate_signal(),
                indent=2
            )
        )

        time.sleep(2)

