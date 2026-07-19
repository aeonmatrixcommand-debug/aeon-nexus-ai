class AgentMemory:
    """
    Shared memory between AI agents.
    """

    def __init__(self):
        self.memory = []

    def store(self, agent, knowledge):

        self.memory.append({
            "agent": agent,
            "knowledge": knowledge
        })

        return "stored"

    def recall(self):
        return self.memory
