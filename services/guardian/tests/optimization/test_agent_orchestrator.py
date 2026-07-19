
from services.guardian.agents.orchestrator import (
    AgentOrchestrator
)


def test_agent():

    r=AgentOrchestrator().dispatch(
        "Demand Prediction"
    )

    assert r.agent_name
