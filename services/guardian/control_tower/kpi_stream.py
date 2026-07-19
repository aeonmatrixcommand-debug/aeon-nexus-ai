from datetime import datetime


class KPIStream:

    def publish(self, metrics):

        return {
            "type": "KPI_UPDATE",
            "metrics": metrics,
            "timestamp": datetime.utcnow().isoformat()
        }
