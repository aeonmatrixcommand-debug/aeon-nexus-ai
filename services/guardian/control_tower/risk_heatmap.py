class RiskHeatmap:

    def analyze(self, signals):

        score = signals.get(
            "risk_score",
            0
        )

        level = (
            "CRITICAL"
            if score >= 80
            else "WARNING"
            if score >= 50
            else "NORMAL"
        )

        return {
            "risk_score": score,
            "risk_level": level
        }
