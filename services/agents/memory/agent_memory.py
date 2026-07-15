class AgentMemory:

    def __init__(self):
        self.memory_store = {}

    def remember(self, key, value):
        self.memory_store[key] = value

    def recall(self, key):
        return self.memory_store.get(key)
