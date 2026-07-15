from api.decision_service import DecisionService


class EnterpriseGateway:
    """
    Entry point for enterprise systems.
    """

    def __init__(self):

        self.service = DecisionService()


    def execute_decision(
        self,
        event,
        decision
    ):

        return self.service.analyze(
            event,
            decision
        )
