from .policy.policy_engine import evaluate
from .risk.risk_engine import assess
from .compliance.compliance_validator import validate
from .audit.audit_logger import record
from .memory.governance_memory import save


policy = evaluate(
    "AUTONOMOUS_DECISION"
)

risk = assess(
    policy
)

compliance = validate(
    risk
)

audit = record(
    compliance
)

print(policy)
print(risk)
print(compliance)
print(audit)
print(save(audit))
