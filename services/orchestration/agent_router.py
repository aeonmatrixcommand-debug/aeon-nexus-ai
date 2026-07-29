class AgentRouter:

    def route(self, task):
        return {
            "task": task,
            "agent": "selected"
        }
