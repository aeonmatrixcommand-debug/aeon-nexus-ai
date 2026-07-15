
class AgentMemoryStore:

    def __init__(self):
        self.storage = {}

    def save(
        self,
        agent_id,
        memory
    ):
        if agent_id not in self.storage:
            self.storage[agent_id] = []

        self.storage[agent_id].append(memory)

    def get(
        self,
        agent_id
    ):
        return self.storage.get(agent_id, [])

    def latest(
        self,
        agent_id
    ):
        memories = self.get(agent_id)

        if not memories:
            return None

        return memories[-1]

