class AgentPolicy:

    def __init__(self):
        self.rules = {
            "high_risk_requires_approval": True
        }

    def validate(self, agent):

        if agent.risk_level == "high":
            return False

        return True
