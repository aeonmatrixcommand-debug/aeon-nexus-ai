class IntentEngine:

    def analyze(self, query):

        query_lower = query.lower()

        if "risk" in query_lower:
            intent = "risk_analysis"

        elif "inventory" in query_lower:
            intent = "inventory_analysis"

        elif "forecast" in query_lower:
            intent = "demand_forecast"

        else:
            intent = "general_business_question"


        return {
            "query": query,
            "intent": intent,
            "confidence": 0.92
        }
