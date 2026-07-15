from multi_agent.specialist_agents import (
    RiskAgent,
    OperationAgent,
    FinanceAgent,
    ExecutiveAgent
)

from multi_agent.consensus_engine import ConsensusEngine


class MultiAgentRuntime:


    def __init__(self):

        self.risk = RiskAgent()
        self.operation = OperationAgent()
        self.finance = FinanceAgent()
        self.executive = ExecutiveAgent()
        self.consensus = ConsensusEngine()



    def analyze(self, context):

        opinions = [

            self.risk.analyze(context),

            self.operation.analyze(context),

            self.finance.analyze(context)

        ]


        consensus = self.consensus.decide(
            opinions
        )


        executive = self.executive.summarize(
            opinions
        )


        return {

            "agent_opinions":opinions,

            "consensus":consensus,

            "executive_summary":executive

        }
