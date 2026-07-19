from .policy.policy_engine import evaluate_policy
from .compliance.compliance_validator import validate
from .risk.risk_approval import approve
from .decision.governance_log import record
from .memory.policy_memory import save


policy = evaluate_policy(
    "AUTONOMOUS_INVENTORY_DECISION"
)

compliance = validate(
    policy
)

risk = approve(
    15
)

decision = record(
    risk
)

print(policy)
print(compliance)
print(risk)
print(decision)
print(save(decision))
