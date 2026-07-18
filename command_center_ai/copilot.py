import requests
from datetime import datetime


class CommandCenterCopilot:

    def __init__(self):
        self.gateway = "http://127.0.0.1:8080/generate"


    def analyze(self, telemetry):

        prompt = f"""
AEON MATRIX REAL-TIME COMMAND CENTER

Timestamp:
{datetime.now().isoformat()}

Telemetry Event:
{telemetry}

Generate Executive Intelligence:

1. Current Situation
2. Risk Analysis
3. Root Cause Prediction
4. Recommended Action
5. Human Approval Required
6. Business Impact
7. Autonomous Decision
"""

        response = requests.post(
            self.gateway,
            json={"prompt": prompt},
            timeout=120
        )

        return response.json()


if __name__ == "__main__":

    copilot = CommandCenterCopilot()

    telemetry = """
Source: WMS
Event: Warehouse DC Alert

Inventory mismatch detected
Order delay increasing
Driver ETA unstable
OTIF risk detected
"""

    result = copilot.analyze(telemetry)

    print("=================================")
    print(" AEON MATRIX COMMAND CENTER AI ")
    print("=================================")

    print(result.get("response"))

    print("=================================")
    print(" REAL-TIME COPILOT ONLINE ")
    print("=================================")
