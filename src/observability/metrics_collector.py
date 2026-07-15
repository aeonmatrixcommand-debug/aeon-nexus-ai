class MetricsCollector:
    """
    Collect AI operational metrics.
    """

    def __init__(self):

        self.metrics = []


    def record(self, name, value):

        metric = {
            "metric": name,
            "value": value,
            "status": "captured"
        }

        self.metrics.append(metric)

        return metric


    def snapshot(self):

        return {
            "metrics": self.metrics,
            "count": len(self.metrics),
            "status": "healthy"
        }
