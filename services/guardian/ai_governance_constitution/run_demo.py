from .constitution.ai_constitution import load
from .policy.policy_engine import validate
from .gateway.decision_gate import check
from .audit.audit_logger import record
from .memory.governance_memory import save


constitution = load()

policy = validate(
    "AUTONOMOUS_INVENTORY_ACTION"
)

gate = check(
    policy
)

audit = record(
    "AI_DECISION_EXECUTION"
)

print(constitution)
print(policy)
print(gate)
print(audit)
print(save(gate))
