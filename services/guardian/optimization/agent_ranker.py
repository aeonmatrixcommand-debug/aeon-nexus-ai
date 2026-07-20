class AgentRanker:

    def rank(self, agents):

        return sorted(
            agents,
            key=lambda x: x.get(
                "performance",
                0
            ),
            reverse=True
        )
