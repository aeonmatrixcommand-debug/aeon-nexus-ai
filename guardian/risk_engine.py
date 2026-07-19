class RiskEngine:


    def evaluate(self, event):

        score = 0


        text = event.lower()


        if "inventory" in text:
            score += 30


        if "delay" in text:
            score += 25


        if "eta" in text:
            score += 20


        if score >= 70:
            level = "HIGH"

        elif score >= 40:
            level = "MEDIUM"

        else:
            level = "LOW"


        return {
            "risk_score": score,
            "risk_level": level
        }
