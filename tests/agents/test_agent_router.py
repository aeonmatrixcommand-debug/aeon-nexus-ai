from services.agents.registry.agent_registry import AgentRegistry
from services.agents.registry.agent_metadata import AgentMetadata
from services.agents.orchestration.agent_router import AgentRouter


def test_agent_router_selects_correct_agent():

    registry = AgentRegistry()

    wms_agent = AgentMetadata(
        name="wms_agent",
        version="1.0",
        capabilities=[
            "inventory_check",
            "stock_analysis"
        ]
    )

    sales_agent = AgentMetadata(
        name="sales_agent",
        version="1.0",
        capabilities=[
            "recommend_product"
        ]
    )

    registry.register(wms_agent)
    registry.register(sales_agent)

    router = AgentRouter(registry)

    result = router.route("inventory_check")

    assert result is not None
    assert result.name == "wms_agent"
