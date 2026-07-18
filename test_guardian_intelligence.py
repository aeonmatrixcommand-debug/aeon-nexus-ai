from guardian.risk_engine import RiskEngine
from guardian.governance import GovernanceEngine
from guardian.audit_store import AuditStore


event = """
Warehouse DC:
Inventory mismatch detected
Order delay increasing
Driver ETA unstable
"""


risk = RiskEngine()

gov = GovernanceEngine()

store = AuditStore()


result = {

    "event": event,

    "risk": risk.evaluate(event),

    "governance": gov.check(
        "Inventory Re-Sync"
    )

}


print(result)

store.save(result)

print("\nAUDIT MEMORY SAVED")
