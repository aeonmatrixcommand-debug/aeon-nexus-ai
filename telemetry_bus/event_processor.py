from guardian.risk_engine import RiskEngine
from guardian.governance import GovernanceEngine

class EventProcessor:

    def __init__(self):
        self.risk = RiskEngine()
        self.gov = GovernanceEngine()

    def process(self, event):
        return {
            "event": event.to_dict(),
            "risk": self.risk.evaluate(event.payload),
            "governance": self.gov.check("Inventory Re-Sync")
        }
