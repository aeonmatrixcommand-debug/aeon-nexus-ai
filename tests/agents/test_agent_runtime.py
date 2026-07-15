from services.agents.registry.agent_registry import AgentRegistry
from services.agents.registry.agent_metadata import AgentMetadata
from services.agents.orchestration.agent_router import AgentRouter
from services.agents.memory.agent_memory import AgentMemory
from services.agents.governance.agent_policy import AgentPolicy
from services.agents.runtime.agent_runtime import AgentRuntime
from services.agents.runtime.agent_task import AgentTask


def test_agent_runtime_execution():

    registry = AgentRegistry()

    agent = AgentMetadata(
        name="inventory_agent",
        version="1.0",
        capabilities=[
            "inventory_check"
        ],
        risk_level="low"
    )

    registry.register(agent)

    router = AgentRouter(registry)
    memory = AgentMemory()
    policy = AgentPolicy()

    runtime = AgentRuntime(
        registry,
        router,
        policy,
        memory
    )

    task = AgentTask(
        task_id="task-001",
        capability="inventory_check",
        payload={
            "sku": "SKU001"
        },
        requester="wms"
    )

    result = runtime.execute(task)

    assert result.success is True
    assert result.agent_name == "inventory_agent"

    assert memory.recall("task-001") == {
        "sku": "SKU001"
    }
