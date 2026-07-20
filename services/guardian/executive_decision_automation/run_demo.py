from .decision.decision_engine import analyze
from .action.action_planner import recommend
from .policy.policy_guard import validate
from .approval.approval_router import route
from .memory.decision_memory import save


decision = analyze(
    "INVENTORY_RISK_SIGNAL"
)

action = recommend(
    decision
)

policy = validate(
    action
)

approval = route(
    policy
)

print(decision)
print(action)
print(policy)
print(approval)
print(save(approval))
