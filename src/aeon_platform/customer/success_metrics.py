"""
AEON MATRIX Customer Success Metrics
Sprint 90
"""


class SuccessMetrics:


    def calculate(
        self,
        metrics,
    ):

        return {
            "metrics": metrics,
            "health_score":
                sum(metrics.values()) /
                len(metrics),
        }
