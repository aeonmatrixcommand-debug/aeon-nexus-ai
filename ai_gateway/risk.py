class RiskAnalyzer:

    def __init__(self):
        self.rules = {
            "temperature": 80,
            "inventory": 70,
            "security": 90,
            "failure": 85
        }


    def analyze(self, event):

        text = event.lower()

        score = 0
        category = "normal"


        for key, value in self.rules.items():

            if key in text:
                score = max(
                    score,
                    value
                )
                category = key


        if score >= 85:
            level = "CRITICAL"

        elif score >= 70:
            level = "HIGH"

        elif score > 0:
            level = "MEDIUM"

        else:
            level = "LOW"


        return {
            "risk_level": level,
            "score": score,
            "category": category
        }
