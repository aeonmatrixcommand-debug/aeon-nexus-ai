from datetime import datetime


class DigitalTwinSimulator:

    def simulate(self, scenario):

        return {
            "scenario": scenario,
            "inventory_state": "CALCULATED",
            "fleet_state": "OPTIMIZED",
            "warehouse_state": "BALANCED",
            "confidence": "HIGH",
            "timestamp": datetime.utcnow().isoformat()
        }
