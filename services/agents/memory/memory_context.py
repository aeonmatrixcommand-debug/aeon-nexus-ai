
class AgentMemoryContext:

    def __init__(
        self,
        store
    ):
        self.store = store


    def build_context(
        self,
        agent_id,
        current_task
    ):

        history = self.store.get(agent_id)

        return {
            "agent_id": agent_id,
            "history": history,
            "current_task": current_task
        }

