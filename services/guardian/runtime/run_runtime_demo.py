from services.guardian.runtime.orchestration.runtime_orchestrator import RuntimeOrchestrator


runtime = RuntimeOrchestrator()

event = runtime.execute(
    "Inventory Risk Prediction"
)

print({
    "runtime_status": "ACTIVE",
    "event": event
})
