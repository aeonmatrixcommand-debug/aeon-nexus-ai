from src.intelligence.os.enterprise_runtime import (
    EnterpriseRuntime,
)

from src.intelligence.executive.command_intelligence import (
    ExecutiveCommand,
)

from src.intelligence.autonomy.decision_loop import (
    AutonomousDecisionLoop,
)


def test_enterprise_runtime():

    runtime = EnterpriseRuntime(
        "mother_brain",
        "multi_agent",
        "governance",
        "digital_twin",
    )

    result = runtime.status()

    assert result["enterprise_ready"]


def test_command_intelligence():

    result = ExecutiveCommand().generate_insight(
        {
            "OTIF": 98,
            "risk": "low",
        }
    )

    assert result["decision_ready"]


def test_autonomous_loop():

    result = AutonomousDecisionLoop().execute(
        "inventory_risk"
    )

    assert result["action_generated"]
