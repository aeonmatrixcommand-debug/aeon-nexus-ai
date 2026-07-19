from services.guardian.control_tower.kpi_stream import KPIStream
from services.guardian.control_tower.risk_heatmap import RiskHeatmap
from services.guardian.control_tower.governance_gate import GovernanceGate
from services.guardian.control_tower.executive_feed import ExecutiveFeed


class EnterpriseControlTower:

    def __init__(self):
        self.kpi = KPIStream()
        self.risk = RiskHeatmap()
        self.policy = GovernanceGate()
        self.executive = ExecutiveFeed()

    def monitor(self, event):

        return {
            "kpi": self.kpi.publish(event),
            "risk": self.risk.analyze(event),
            "governance": self.policy.approve(
                event.get("action")
            ),
            "executive": self.executive.create(event)
        }
