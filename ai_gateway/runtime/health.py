class SystemHealth:

    def check(self, mode=None, provider=None):
        return {
            "gateway": "ONLINE",
            "guardian": "ONLINE",
            "executor": "ONLINE",
            "runtime": "ONLINE",
            "mode": mode,
            "provider": provider
        }
