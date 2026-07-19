from .engine.response_engine import create
from .action.action_planner import plan
from .policy.policy_validator import validate
from .workflow.workflow_engine import execute
from .outcome.outcome_tracker import track
from .memory.response_memory import save


alert = {
    "type": "INVENTORY_RISK",
    "risk_score": 91
}


response = create(alert)

action = plan(response)

policy = validate(action)

workflow = execute(action)

outcome = track(workflow)

memory = save(
    {
        "response": response,
        "action": action,
        "policy": policy,
        "workflow": workflow,
        "outcome": outcome
    }
)


print(response)
print(action)
print(policy)
print(workflow)
print(outcome)
print(memory)
