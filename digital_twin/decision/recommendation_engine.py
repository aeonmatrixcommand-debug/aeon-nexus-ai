class RecommendationEngine:
    """
    Select best decision based on impact.
    """

    def recommend(self, simulations):

        best = None
        score = -1

        for item in simulations:

            current = item["risk_reduction"] - (item["cost"] / 100000)

            if current > score:
                score = current
                best = item

        return best
