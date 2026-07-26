class MemoryNetwork:

    def __init__(self):
        self.memory = []

    def store(self, item):
        self.memory.append(item)

    def recall(self):
        return self.memory
