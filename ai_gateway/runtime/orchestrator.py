class RuntimeOrchestrator:

    def __init__(
        self,
        lifecycle,
        events,
        feedback,
        health,
        executor
    ):
        self.lifecycle = lifecycle
        self.events = events
        self.feedback = feedback
        self.health = health
        self.executor = executor


    def execute(self, action):

        self.lifecycle.move("APPROVED")

        self.events.emit({
            "type": "ACTION_APPROVED",
            "action": action
        })


        self.lifecycle.move("EXECUTING")

        result = self.executor.execute(action)


        self.lifecycle.move("COMPLETED")


        self.feedback.capture(
            action,
            result
        )


        self.events.emit({
            "type": "ACTION_COMPLETED",
            "result": result
        })


        return result
