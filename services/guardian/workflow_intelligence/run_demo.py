from services.guardian.workflow_intelligence.discovery.process_discovery import discover
from services.guardian.workflow_intelligence.generator.workflow_generator import generate
from services.guardian.workflow_intelligence.execution.task_executor import execute
from services.guardian.workflow_intelligence.monitor.workflow_monitor import monitor
from services.guardian.workflow_intelligence.memory.process_memory import save


process = discover(
    "ORDER_FULFILLMENT_PROCESS"
)

workflow = generate(
    process
)

execution = execute(
    workflow
)

health = monitor(
    execution
)

print(process)
print(workflow)
print(execution)
print(health)
print(save(health))
