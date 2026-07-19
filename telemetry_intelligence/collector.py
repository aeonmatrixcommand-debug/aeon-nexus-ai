from datetime import datetime


class TelemetryCollector:

    def collect(self, source, metrics):

        return {
            "source": source,
            "metrics": metrics,
            "status": "INGESTED",
            "timestamp": datetime.utcnow().isoformat()
        }
