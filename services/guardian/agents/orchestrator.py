
from services.guardian.agents.registry import (
    AgentRegistry
)

from services.guardian.contracts.agent_event import (
    AgentEvent
)


registry=AgentRegistry()


registry.register(
    "Forecast Agent",
    "Demand Prediction"
)

registry.register(
    "Risk Agent",
    "Risk Analysis"
)

registry.register(
    "Optimization Agent",
    "Resource Allocation"
)



class AgentOrchestrator:


    def dispatch(
        self,
        task
    ):


        for agent,data in registry.list_agents().items():

            if data["capability"] in task:

                return AgentEvent(

                    agent,

                    task,

                    "EXECUTE",

                    0.94,

                    0.90

                )


        return AgentEvent(

            "Optimization Agent",

            task,

            "EXECUTE",

            0.85,

            0.75

        )
