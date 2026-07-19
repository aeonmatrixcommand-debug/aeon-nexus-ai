class ImpactScoreEngine:

    def calculate(self, prediction, risk):

        score = (
            prediction.get("impact_score", 0)
            * (1 - risk.get("risk_score", 0))
        )

        return {
            "business_impact_score": round(score, 2),
            "priority":
                "HIGH" if score >= 0.7 else "NORMAL"
        }
