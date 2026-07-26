class AgentReputation:


    def evaluate(
        self,
        profile
    ):

        if profile.rating >= 0.8:
            level = "TRUSTED"

        elif profile.rating >= 0.5:
            level = "VERIFIED"

        else:
            level = "NEW"


        return {
            "agent": profile.agent_id,
            "rating": profile.rating,
            "level": level
        }
