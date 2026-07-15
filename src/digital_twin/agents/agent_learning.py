class AgentLearning:
    """
    Learn from agent execution outcomes.
    """

    def learn(self, action, outcome):

        return {
            "action": action,
            "outcome": outcome,
            "learning": "updated"
        }
