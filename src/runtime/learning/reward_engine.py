class RewardEngine:
    """
    Evaluate autonomous action outcomes.
    """

    def calculate(self, action, result):

        reward = 0.0

        if result.get("status") == "executed":
            reward += 0.8

        if result.get("result") == "success":
            reward += 0.2

        return {
            "action": action,
            "reward": reward,
            "quality": "positive" if reward >= 0.8 else "needs_improvement"
        }
