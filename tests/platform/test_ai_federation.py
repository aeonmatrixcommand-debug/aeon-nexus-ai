from src.aeon_platform.federation.agent_registry import (
    AgentRegistry,
)

from src.aeon_platform.federation.trust_engine import (
    AgentTrustEngine,
)

from src.aeon_platform.federation.exchange_hub import (
    ExchangeHub,
)


def test_agent_registry():

    agent = AgentRegistry().register(
        "fleet_ai",
        "partner_company",
    )

    result = AgentRegistry().lookup(
        agent,
    )

    assert result["trusted"]


def test_trust_engine():

    result = AgentTrustEngine().evaluate(
        "fleet_ai",
        0.95,
    )

    assert result["approved"]


def test_exchange():

    result = ExchangeHub().exchange(
        "aeon_agent",
        "partner_agent",
        "route_signal",
    )

    assert result["delivered"]
