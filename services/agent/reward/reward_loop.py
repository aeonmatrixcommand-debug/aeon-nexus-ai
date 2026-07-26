class RewardLoop:

    def evaluate(self, action, outcome):

        score = 1.0 if outcome == "SUCCESS" else 0.0

        return {
            "action": action,
            "reward": score
        }
