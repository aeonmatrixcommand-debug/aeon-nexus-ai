"""
AEON MATRIX Executive KPI Intelligence
Sprint 81
"""


class ExecutiveKPIEngine:

    def evaluate(
        self,
        otif: float,
        sla: float,
        risk: float,
    ) -> dict:

        health_score = round(
            (otif + sla + (1 - risk)) / 3,
            2,
        )

        return {
            "health_score": health_score,
            "otif": otif,
            "sla": sla,
            "risk": risk,
        }
