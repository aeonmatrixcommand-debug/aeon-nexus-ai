from mother_brain.decision import DecisionEngine
from guardian.audit import AuditLogger


engine = DecisionEngine()
audit = AuditLogger()

actions = [
    "Inventory Re-Sync",
    "Route Change Request",
    "Weight Verification Override"
]


for action in actions:

    result = engine.process(action)

    print("\nACTION:", action)

    print(audit.log(
        action,
        result
    ))
