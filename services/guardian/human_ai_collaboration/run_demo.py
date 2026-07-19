from .workforce.workforce_engine import analyze
from .skill.skill_mapper import map_skill
from .assignment.task_assignment import assign
from .monitor.collaboration_monitor import monitor
from .memory.workforce_memory import save


team = analyze(
    "WAREHOUSE_OPERATION_TEAM"
)

skill = map_skill(
    "OPERATION_MANAGER"
)

assignment = assign(
    "INVENTORY_DECISION_REVIEW",
    "HUMAN_SUPERVISOR"
)

collaboration = monitor(
    assignment
)

print(team)
print(skill)
print(assignment)
print(collaboration)
print(save(collaboration))
