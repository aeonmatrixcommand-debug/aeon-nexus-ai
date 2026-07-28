class RecommendationEngine:

    def recommend(self, options):
        return {
            "recommendation": options[0] if options else None
        }
