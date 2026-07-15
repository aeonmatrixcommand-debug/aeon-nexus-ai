class AgentRegistry:
    """
    Register enterprise AI agents.
    """

    def __init__(self):

        self.agents = {
            "risk_agent": "Risk Analysis Specialist",
            "operation_agent": "Operational Optimization Specialist",
            "finance_agent": "Cost Impact Specialist",
            "executive_agent": "Executive Decision Specialist"
        }


    def list_agents(self):

        return self.agents
