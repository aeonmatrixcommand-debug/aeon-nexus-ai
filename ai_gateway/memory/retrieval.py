
class MemoryRetriever:

    def __init__(self, store):
        self.store = store


    def search(self, keyword):

        results = []

        for item in self.store.recall():

            if keyword in str(item):
                results.append(item)

        return results
