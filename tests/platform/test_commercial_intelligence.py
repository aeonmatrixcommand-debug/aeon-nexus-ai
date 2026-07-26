from src.aeon_platform.commercial.usage_analytics import (
    UsageAnalytics,
)

from src.aeon_platform.commercial.billing_engine import (
    BillingEngine,
)

from src.aeon_platform.commercial.revenue_intelligence import (
    RevenueIntelligence,
)


def test_usage():

    result = UsageAnalytics().analyze(
        [
            "order",
            "inventory",
        ]
    )

    assert result["active_usage"]


def test_billing():

    result = BillingEngine().calculate(
        100,
        5,
    )

    assert result["amount"] == 500


def test_revenue():

    result = RevenueIntelligence().forecast(
        10,
        1000,
    )

    assert result["forecast"] == 10000
