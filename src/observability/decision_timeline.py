class DecisionTimeline:

    """
    Store AI decision journey.
    """


    def __init__(self):

        self.events = []


    def add(self, stage, result):

        self.events.append(
            {
                "stage": stage,
                "result": result
            }
        )


        return self.events
