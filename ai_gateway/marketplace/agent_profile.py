from datetime import datetime


class AgentProfile:


    def __init__(
        self,
        agent_id,
        capability
    ):

        self.agent_id = agent_id
        self.capability = capability
        self.rating = 0.0
        self.executions = 0
        self.created = datetime.utcnow().isoformat()



    def update_rating(
        self,
        score
    ):

        self.executions += 1

        self.rating = (
            (
                self.rating *
                (self.executions - 1)
            )
            +
            score
        ) / self.executions



    def to_dict(self):

        return {
            "agent_id": self.agent_id,
            "capability": self.capability,
            "rating": self.rating,
            "executions": self.executions,
            "created": self.created
        }
