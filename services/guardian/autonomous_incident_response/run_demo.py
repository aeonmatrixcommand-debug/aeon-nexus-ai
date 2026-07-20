from .detection.incident_detector import detect
from .severity.severity_analyzer import analyze
from .recovery.recovery_planner import plan
from .guardian.guardian_gate import approve
from .memory.incident_memory import save


incident = detect(
    "SERVICE_LATENCY_SPIKE"
)

severity = analyze(
    incident
)

recovery = plan(
    severity
)

approval = approve(
    recovery
)

print(incident)
print(severity)
print(recovery)
print(approval)
print(save(approval))
