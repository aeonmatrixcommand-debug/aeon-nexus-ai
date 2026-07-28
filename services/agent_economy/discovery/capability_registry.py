class CapabilityRegistry:

    def register(self, agent, capability):
        return {
            "agent": agent,
            "capability": capability,
            "registered": True
        }

    def discover(self, capability):
        return {
            "capability": capability,
            "agents": ["available"]
        }
