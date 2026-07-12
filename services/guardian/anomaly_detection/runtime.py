class AnomalyDetection:
    def analyze(self, metric):
        return {
            "anomaly": metric > 90
        }
