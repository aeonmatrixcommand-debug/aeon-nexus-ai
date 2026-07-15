from services.agents.marketplace.agent_catalog import AgentCatalog
from services.agents.marketplace.capability_index import CapabilityIndex
from services.agents.marketplace.agent_discovery import AgentDiscovery


def test_agent_catalog_register():

    catalog = AgentCatalog()

    catalog.register(
        name="WMS_AGENT",
        capabilities=[
            "inventory_check",
            "warehouse_operation"
        ]
    )

    agent = catalog.get("WMS_AGENT")

    assert agent["name"] == "WMS_AGENT"


def test_capability_index_search():

    index = CapabilityIndex()

    index.add(
        "forecast",
        "DEMAND_FORECAST_AGENT"
    )

    result = index.search("forecast")

    assert result == "DEMAND_FORECAST_AGENT"


def test_agent_discovery():

    catalog = AgentCatalog()
    index = CapabilityIndex()

    catalog.register(
        name="LANGUAGE_AGENT",
        capabilities=[
            "translation"
        ]
    )

    index.add(
        "translation",
        "LANGUAGE_AGENT"
    )

    discovery = AgentDiscovery(
        catalog,
        index
    )

    agent = discovery.find("translation")

    assert agent["name"] == "LANGUAGE_AGENT"
