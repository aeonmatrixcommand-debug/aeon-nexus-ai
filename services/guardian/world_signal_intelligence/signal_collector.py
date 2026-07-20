from datetime import datetime


class WorldSignalCollector:

    def collect(self, signals):

        return {
            "market_signal": signals.get("market_signal"),
            "supply_signal": signals.get("supply_signal"),
            "demand_signal": signals.get("demand_signal"),
            "timestamp": datetime.utcnow().isoformat()
        }
