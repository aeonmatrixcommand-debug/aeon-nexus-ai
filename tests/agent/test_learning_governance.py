from services.agent.governance.audit import (
    LearningAuditRecord,
    LearningAuditTrail,
)
from services.agent.governance.policy import (
    LearningPolicyEngine,
)


def test_learning_audit_record():
    trail = LearningAuditTrail()

    record = LearningAuditRecord(
        agent_id="AEON-001",
        event="reward_update",
        previous_score=0.8,
        new_score=0.95,
        reason="accuracy_improved",
    )

    trail.record(record)

    assert trail.latest().agent_id == "AEON-001"
    assert trail.latest().new_score == 0.95


def test_learning_policy():
    engine = LearningPolicyEngine()

    assert engine.evaluate(0.95) is True
    assert engine.evaluate(0.5) is False
