from .metrics.metrics_engine import collect_metrics
from .health.service_health import check_service
from .incident.incident_detector import detect_incident
from .reliability.reliability_score import calculate_score
from .recovery.recovery_signal import create_recovery_signal


metrics = collect_metrics(
    "AEON MATRIX CORE"
)

incident = detect_incident(
    metrics
)

print(metrics)
print(check_service(metrics))
print(incident)
print(calculate_score(metrics))
print(create_recovery_signal(incident))
