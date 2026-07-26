from src.intelligence.observability.model_monitor import (
    ModelMonitor,
)

from src.intelligence.governance.decision_quality import (
    DecisionQualityEngine,
)

from src.intelligence.governance.policy_monitor import (
    PolicyMonitor,
)

from src.intelligence.executive.trust_dashboard import (
    TrustDashboard,
)


def test_model_monitor():

    health = ModelMonitor().evaluate(
        "mother_brain",
        0.95,
        120,
    )

    assert health.healthy


def test_decision_quality():

    score = DecisionQualityEngine().score(
        0.95,
        0.90,
    )

    assert score > 0.8


def test_policy_monitor():

    result = PolicyMonitor().check(
        "delete_inventory",
        False,
    )

    assert result["blocked"]


def test_trust_dashboard():

    dashboard = TrustDashboard().generate(
        True,
        0.9,
    )

    assert dashboard["trust_ready"]
