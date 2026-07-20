class RecommendationEngine:

    def recommend(self, prediction):

        if prediction["impact_score"] > 0.8:
            return "INCREASE_ALLOCATION"

        return "MAINTAIN_STOCK"
