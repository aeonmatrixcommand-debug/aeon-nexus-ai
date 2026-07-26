class AgentHealth:


    def check(self, agent):

        return {
            "agent": agent.agent_id,
            "status": agent.status,
            "healthy": True
        }
