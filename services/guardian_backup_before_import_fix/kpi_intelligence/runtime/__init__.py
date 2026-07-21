"""
AEON MATRIX KPI Intelligence Runtime

Decision Intelligence Layer
OTIF SLA Productivity Risk Profit
"""


class KPIIntelligenceEngine:

    def __init__(self):
        self.name = "AEON MATRIX KPI Intelligence Engine"
        self.metrics = {}


    def record(self, key, value):
        self.metrics[key] = value
        return self.metrics


    def get(self, key, default=None):
        return self.metrics.get(key, default)


    def evaluate(self, metrics):

        otif = metrics.get("otif", 0)
        sla = metrics.get("sla", 0)

        score = (otif + sla) / 2


        otif_status = (
            "healthy"
            if otif >= 95
            else "risk"
        )

        sla_status = (
            "healthy"
            if sla >= 95
            else "risk"
        )


        if score >= 95:
            status = "excellent"
            risk = "low"
        elif score >= 85:
            status = "stable"
            risk = "medium"
        else:
            status = "attention_required"
            risk = "high"


        return {
            "engine": self.name,

            "score": score,

            "status": status,

            "risk": risk,

            "otif_status": otif_status,

            "sla_status": sla_status,

            "metrics": metrics
        }


    def health(self):

        return {
            "status": "healthy",
            "engine": self.name
        }
