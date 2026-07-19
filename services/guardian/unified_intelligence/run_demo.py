from .core.unified_core import initialize
from .integration.system_integrator import integrate
from .orchestration.intelligence_orchestrator import orchestrate
from .learning.unified_learning import learn
from .memory.unified_memory import save


core = initialize(
    "AEON_MATRIX_MOTHER_BRAIN"
)

integration = integrate(
    [
        "TELEMETRY",
        "DIGITAL_TWIN",
        "GOVERNANCE",
        "MULTI_AGENT",
        "WORKFLOW",
        "DECISION",
        "OUTCOME"
    ]
)

operation = orchestrate(
    integration
)

learning = learn(
    operation
)

print(core)
print(integration)
print(operation)
print(learning)
print(save(learning))
