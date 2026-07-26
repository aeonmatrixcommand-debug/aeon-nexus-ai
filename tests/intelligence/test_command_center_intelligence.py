from src.intelligence.command_center.runtime import (
    CommandCenterRuntime,
)

from src.intelligence.kpi.executive_kpi import (
    ExecutiveKPIEngine,
)

from src.intelligence.governance.human_ai_bridge import (
    HumanAIBridge,
)


def test_command_center_runtime():

    signal = CommandCenterRuntime().create_signal(
        "digital_twin",
        "high",
        "warehouse capacity risk",
    )

    assert signal.priority == "high"


def test_executive_kpi():

    result = ExecutiveKPIEngine().evaluate(
        0.95,
        0.98,
        0.10,
    )

    assert result["health_score"] > 0


def test_human_ai_bridge():

    approval = HumanAIBridge().request_approval(
        "reroute shipment",
        0.85,
    )

    assert approval["approval_required"]
