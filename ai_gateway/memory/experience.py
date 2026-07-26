
class ExperienceMemory:

    def __init__(self, store):
        self.store = store


    def learn(self, action, result):

        self.store.remember({
            "action": action,
            "result": result
        })
