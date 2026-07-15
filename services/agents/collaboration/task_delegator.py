class TaskDelegator:

    def delegate(
        self,
        task,
        agent
    ):

        return {
            "task": task,
            "agent": agent,
            "status": "delegated"
        }
