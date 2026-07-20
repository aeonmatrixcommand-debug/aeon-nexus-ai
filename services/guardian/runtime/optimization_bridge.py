
from services.guardian.agents.orchestrator import (
    AgentOrchestrator
)

from services.guardian.optimization.engine import (
    OptimizationEngine
)



orchestrator=AgentOrchestrator()

optimizer=OptimizationEngine()



def optimize_operation(context):


    agent_event = orchestrator.dispatch(
        "Demand Prediction"
    )


    optimization = optimizer.optimize(

        context["inventory"],

        context["demand"],

        context["capacity"]

    )


    return {

        "agent":
            agent_event.to_dict(),

        "optimization":
            optimization

    }
