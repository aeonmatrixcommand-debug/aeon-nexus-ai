<<<<<<< HEAD
from .core.unified_core import initialize
from .integration.system_integrator import integrate
from .orchestration.intelligence_orchestrator import orchestrate
from .learning.unified_learning import learn
from .memory.unified_memory import save
=======
from services.guardian.unified_intelligence.core.unified_core import initialize
from services.guardian.unified_intelligence.integration.system_integrator import integrate
from services.guardian.unified_intelligence.orchestration.intelligence_orchestrator import orchestrate
from services.guardian.unified_intelligence.learning.unified_learning import learn
from services.guardian.unified_intelligence.memory.unified_memory import save
>>>>>>> 1df4713 (fix: migrate guardian imports to services namespace)


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
