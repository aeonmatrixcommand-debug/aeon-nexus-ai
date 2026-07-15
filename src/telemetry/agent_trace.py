class AgentTrace:

    def trace(self, agent, action):

        return {
            "agent": agent,
            "action": action,
            "status": "tracked"
        }
