class AIExplanation:

    def explain(self, analysis):

        return {
            "summary":
                f"Situation caused by {analysis.get('cause')}",

            "impact":
                analysis.get("impact"),

            "recommended_focus":
                analysis.get("opportunity")
        }
