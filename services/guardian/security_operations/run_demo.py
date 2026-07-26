from .incident.incident_detector import detect
from .risk.risk_engine import score
from .alert.alert_manager import notify
from .response.response_engine import respond
from .memory.security_memory import save

incident = detect(
    "UNAUTHORIZED_API_ACCESS"
)

risk = score(
    incident
)

alert = notify(
    risk
)

response = respond(
    alert
)

memory = save(
    response
)

print(incident)
print(risk)
print(alert)
print(response)
print(memory)
