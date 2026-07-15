from agent_marketplace.agent_registry import AgentRegistry
from agent_marketplace.discovery_engine import DiscoveryEngine
from agent_marketplace.agent_bus import AgentBus



class AgentMarketplaceRuntime:


    def __init__(self):

        self.registry=AgentRegistry()
        self.discovery=DiscoveryEngine()
        self.bus=AgentBus()



    def setup(self):

        self.registry.register(
            "risk_agent",
            "risk_detection"
        )

        self.registry.register(
            "forecast_agent",
            "demand_prediction"
        )

        self.registry.register(
            "finance_agent",
            "cost_analysis"
        )



    def execute(self,task):


        agents=self.discovery.discover(task)


        responses=[]


        for agent in agents["recommended_agents"]:

            responses.append(

                self.bus.send(
                    agent,
                    task
                )

            )


        return {

            "discovery":agents,

            "responses":responses,

            "available_agents":
            self.registry.list_agents(),

            "status":
            "enterprise_agent_ready"

        }
