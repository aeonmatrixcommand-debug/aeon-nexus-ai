class RuntimeRegistry:
    def __init__(self):
        self.services = {}

    def register(self, name, service):
        self.services[name] = service

    def status(self):
        return {
            name: "READY" for name in self.services
        }

registry = RuntimeRegistry()
