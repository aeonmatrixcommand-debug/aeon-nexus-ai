from services.agents.registry.agent_registry import AgentRegistry
from services.agents.registry.agent_metadata import AgentMetadata


def test_agent_registry_register():

    registry = AgentRegistry()

    agent = AgentMetadata(
        name="wms_agent",
        version="1.0",
        capabilities=[
            "inventory_check"
        ],
        tools=[
            "wms_api"
        ]
    )

    registry.register(agent)

    result = registry.get("wms_agent")

    assert result.name == "wms_agent"
    assert "inventory_check" in result.capabilities
