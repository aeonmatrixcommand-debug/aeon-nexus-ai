from .priority.priority_engine import calculate_priority
from .approval.approval_intelligence import approval_route
from .governance.guardian_gate import guardian_validate
from .planner.workflow_planner import create_workflow
from .tracking.action_tracker import track


priority = calculate_priority(
    91,
    88
)

approval = approval_route(
    priority
)

guardian = guardian_validate(
    "OPTIMIZE_INVENTORY"
)

workflow = create_workflow(
    "OPTIMIZE_INVENTORY",
    approval
)

print(priority)
print(approval)
print(guardian)
print(track(workflow))
