class MemoryStore:

    def save(self, experience):
        return {
            "experience": experience,
            "stored": True
        }

    def retrieve(self, query):
        return {
            "query": query,
            "memory": "retrieved"
        }
