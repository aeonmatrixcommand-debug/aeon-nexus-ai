from .registry.agent_registry import register_agent
from .workflow.workflow_engine import create_workflow
from .allocation.task_allocator import allocate
from .guardian.policy_gate import check_policy
from .memory.execution_memory import save_execution


agents = [
    register_agent(
        "Forecast_Agent",
        "Demand Prediction"
    ),
    register_agent(
        "Guardian_Agent",
        "Governance"
    )
]


workflow = create_workflow(
    "Inventory Optimization"
)

task = allocate(
    workflow["workflow"],
    agents
)

policy = check_policy(
    task
)

print(agents)
print(workflow)
print(task)
print(policy)
print(save_execution(policy))
