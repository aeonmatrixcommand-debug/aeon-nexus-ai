from src.intelligence.governance.policy_engine import (
    PolicyEngine,
)

from src.intelligence.governance.audit_runtime import (
    AuditRuntime,
)

from src.intelligence.command_center.decision_trace import (
    CommandDecisionTrace,
)


def test_governance_auto_execute():

    result = PolicyEngine().evaluate(
        "optimize_route",
        0.95,
    )

    assert result["decision"] == "auto_execute"


def test_governance_human_review():

    result = PolicyEngine().evaluate(
        "cancel_order",
        0.70,
    )

    assert result["decision"] == "human_review"


def test_audit_trace():

    audit = AuditRuntime().record(
        "optimize_route",
        "auto_execute",
    )

    trace = CommandDecisionTrace().trace(
        "risk_signal",
        audit.decision,
    )

    assert trace["traceable"]
