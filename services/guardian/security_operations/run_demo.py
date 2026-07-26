<<<<<<< HEAD
from .incident.incident_detector import detect
from .risk.risk_engine import score
from .alert.alert_manager import notify
from .response.response_engine import respond
from .memory.security_memory import save
=======
from services.guardian.security_operations.incident.incident_detector import detect
from services.guardian.security_operations.risk.risk_engine import score
from services.guardian.security_operations.alert.alert_manager import notify
from services.guardian.security_operations.response.response_engine import respond
from services.guardian.security_operations.memory.security_memory import save
>>>>>>> origin/main

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
