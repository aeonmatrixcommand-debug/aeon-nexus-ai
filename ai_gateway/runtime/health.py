class SystemHealth:

    def __init__(self):
        self.last_status = {}

    def check(self, mode=None, provider=None):
        self.last_status = {
            "gateway": "ONLINE",
            "guardian": "ONLINE",
            "executor": "ONLINE",
            "runtime": "ONLINE",
            "runtime_state": "READY",
            "mode": mode,
            "provider": provider
        }

        return self.last_status
