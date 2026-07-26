from src.platform.ecosystem.capability_registry import (
    CapabilityRegistry,
)

from src.platform.ecosystem.partner_gateway import (
    PartnerGateway,
)

from src.platform.ecosystem.plugin_marketplace import (
    PluginMarketplace,
)


def test_capability_registry():

    capability = CapabilityRegistry().register(
        "route_optimization_ai",
        "aeon_partner",
    )

    result = CapabilityRegistry().discover(
        capability,
    )

    assert result["available"]


def test_partner_gateway():

    result = PartnerGateway().connect(
        "logistics_partner",
        "fleet_api",
    )

    assert result["connected"]


def test_plugin_marketplace():

    result = PluginMarketplace().publish(
        "forecast_plugin",
        "1.0.0",
    )

    assert result["published"]
