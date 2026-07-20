from .decision.executive_decision import decide
from .command.command_orchestrator import orchestrate
from .governance.governance_control import validate
from .kpi.kpi_intelligence import analyze
from .memory.executive_memory import save


decision = decide(
    "ENTERPRISE_INTELLIGENCE_SIGNAL"
)

command = orchestrate(
    decision
)

governance = validate(
    command
)

kpi = analyze(
    "BUSINESS_PERFORMANCE"
)

print(decision)
print(command)
print(governance)
print(kpi)
print(save(governance))
