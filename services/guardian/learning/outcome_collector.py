from services.guardian.contracts.outcome_event import OutcomeEvent


class OutcomeCollector:


    def __init__(self):

        self.history=[]


    def record(
        self,
        trace_id,
        decision,
        result,
        success,
        metric
    ):

        event=OutcomeEvent(
            trace_id,
            decision,
            result,
            success,
            metric
        )


        self.history.append(
            event.to_dict()
        )

        return event
