from .policy.policy_engine import validate
from .risk.risk_evaluator import evaluate
from .approval.hitl_manager import request_approval
from .audit.audit_logger import log
from .memory.governance_memory import save


policy = validate(
    "INVENTORY_ADJUSTMENT"
)


risk = evaluate(
    82
)


approval = request_approval(
    "INVENTORY_ADJUSTMENT"
)


audit = log(
    {
        "policy": policy,
        "risk": risk,
        "approval": approval
    }
)


memory = save(
    audit
)


print(policy)
print(risk)
print(approval)
print(audit)
print(memory)
