from src.intelligence.agents.collaboration.coordinator import (
    AgentCoordinator,
)

from src.intelligence.agents.memory.shared_memory import (
    SharedMemory,
)

from src.intelligence.agents.collaboration.negotiation import (
    AgentNegotiator,
)

from src.intelligence.agents.collaboration.workflow import (
    AgentWorkflow,
)


def test_agent_assignment():

    task = AgentCoordinator().assign(
        "logistics_agent",
        "optimize_route",
        "high",
    )

    assert task.agent == "logistics_agent"


def test_shared_memory():

    memory = SharedMemory()

    memory.store(
        "risk",
        "delay_detected",
    )

    assert memory.retrieve("risk") == "delay_detected"


def test_agent_negotiation():

    result = AgentNegotiator().negotiate(
        [
            "warehouse_agent",
            "fleet_agent",
        ],
        "reduce_cost",
    )

    assert result["agreement"]


def test_agent_workflow():

    result = AgentWorkflow().execute(
        [
            "analyze",
            "decide",
            "execute",
        ]
    )

    assert result["completed"]
