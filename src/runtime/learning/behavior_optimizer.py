class BehaviorOptimizer:
    """
    Optimize future autonomous behavior.
    """

    def optimize(self, reward):

        if reward["reward"] >= 0.8:

            return {
                "strategy": "reinforce",
                "learning": "increase_action_preference"
            }

        return {
            "strategy": "adjust",
            "learning": "review_action"
        }
