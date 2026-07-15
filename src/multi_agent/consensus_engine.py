class ConsensusEngine:
    """
    Combine agent opinions.
    """

    def decide(self, opinions):

        score = sum(
            item["score"]
            for item in opinions
        ) / len(opinions)


        return {
            "consensus_score":round(score,2),
            "decision":
                "approved"
                if score >= 0.75
                else "review_required"
        }
