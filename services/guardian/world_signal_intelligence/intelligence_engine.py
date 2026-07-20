class SignalIntelligenceEngine:

    def analyze(self, signal):

        score = 0

        if signal.get("demand_signal") == "HIGH":
            score += 0.4

        if signal.get("supply_signal") == "RISK":
            score += 0.3

        if signal.get("market_signal") == "GROWTH":
            score += 0.3

        return {
            "signal_score": round(score, 2),
            "status":
                "OPPORTUNITY" if score >= 0.7 else "NORMAL"
        }
