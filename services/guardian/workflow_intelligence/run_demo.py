from .discovery.process_discovery import discover
from .generator.workflow_generator import generate
from .execution.task_executor import execute
from .monitor.workflow_monitor import monitor
from .memory.process_memory import save


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
