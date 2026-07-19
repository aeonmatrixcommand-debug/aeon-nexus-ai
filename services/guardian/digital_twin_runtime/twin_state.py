from datetime import datetime


class TwinState:

    def snapshot(self, data):

        return {
            "inventory": data.get("inventory", 0),
            "demand": data.get("demand", 0),
            "risk": data.get("risk", "LOW"),
            "timestamp": datetime.utcnow().isoformat()
        }
