class ServiceRegistry:
    def __init__(self):
        self.services = {}

    def register(self, name, status="READY"):
        self.services[name] = status

    def list_services(self):
        return self.services
