class AgentCapability:


    def __init__(
        self,
        name,
        description,
        category
    ):

        self.name = name
        self.description = description
        self.category = category



    def to_dict(self):

        return {
            "name": self.name,
            "description": self.description,
            "category": self.category
        }
