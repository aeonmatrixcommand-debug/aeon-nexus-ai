from datetime import datetime


class ScenarioGenerator:

    def create(self, context):

        return {
            "scenario_id": "SIM-" + datetime.utcnow().strftime("%Y%m%d%H%M%S"),
            "context": context,
            "status": "GENERATED"
        }
