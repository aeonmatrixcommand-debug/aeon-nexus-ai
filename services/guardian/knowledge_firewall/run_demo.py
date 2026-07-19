from .classification.classifier import classify
from .access.access_control import check_access
from .policy.ai_policy import validate_ai_request
from .guard.knowledge_guard import protect
from .audit.audit_memory import record


data = classify(
    "CUSTOMER INVENTORY REPORT"
)

access = check_access(
    "guardian_agent",
    data["classification"]
)

policy = validate_ai_request(
    "KNOWLEDGE_QUERY"
)

guard = protect(
    data
)

print(data)
print(access)
print(policy)
print(guard)
print(record("AI_KNOWLEDGE_ACCESS"))
