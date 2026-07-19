class AgentMemory:

    def __init__(self):
        self.records = []

    def remember(self, event):
        self.records.append(event)
        return event

    def history(self):
        return self.records


agent_memory = AgentMemory()
