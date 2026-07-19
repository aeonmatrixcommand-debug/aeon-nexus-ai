from .classification.incident_classifier import classify
from .rca.root_cause import analyze
from .recovery.recovery_engine import recover
from .memory.incident_memory import store
from .approval.guardian_gate import approve


event = {
    "name": "API_LATENCY_SPIKE",
    "severity": "HIGH"
}


incident = classify(event)

analysis = analyze(
    incident
)

action = recover(
    analysis
)

approval = approve(
    action
)

print(incident)
print(analysis)
print(action)
print(approval)
print(store(incident))
