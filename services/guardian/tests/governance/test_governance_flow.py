from services.guardian.governance.policy_engine import PolicyEngine
from services.guardian.governance.approval_gate import ApprovalGate
from services.guardian.audit.decision_audit import DecisionAudit


def test_governance_flow():

    decision = {
        "decision": "OPTIMIZE_ALLOCATION",
        "confidence": 0.94,
        "risk_score": 0.1
    }

    policy = PolicyEngine().evaluate(decision)

    assert policy["status"] == "APPROVED"

    approval = ApprovalGate().request(policy)

    assert approval["approved"]

    audit = DecisionAudit().record(decision, policy)

    assert audit["policy_status"] == "APPROVED"
