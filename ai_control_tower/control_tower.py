import json
from datetime import datetime


class KPIAggregator:

    def calculate(self, telemetry):

        return {
            "OTIF": telemetry.get("otif", 0),
            "SLA_HEALTH": telemetry.get("sla_health", 0),
            "INVENTORY_ACCURACY": telemetry.get("inventory_accuracy", 0),
            "ETA_STABILITY": telemetry.get("eta_stability", 0)
        }


class RiskMonitor:

    def evaluate(self, kpi):

        risk = 0

        if kpi["OTIF"] < 90:
            risk += 30

        if kpi["INVENTORY_ACCURACY"] < 95:
            risk += 30

        if kpi["ETA_STABILITY"] < 90:
            risk += 20

        return {
            "risk_score": risk,
            "risk_level": (
                "CRITICAL"
                if risk >= 70
                else "HIGH"
                if risk >= 40
                else "NORMAL"
            )
        }


class DigitalTwinDashboard:

    def generate(self, telemetry):

        kpi = KPIAggregator().calculate(telemetry)
        risk = RiskMonitor().evaluate(kpi)

        return {
            "dashboard_id":
                f"CTRL-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "timestamp":
                datetime.utcnow().isoformat(),

            "kpi":
                kpi,

            "risk":
                risk,

            "digital_twin_status":
                "SYNCHRONIZED"
        }


if __name__ == "__main__":

    telemetry = {
        "otif": 86,
        "sla_health": 88,
        "inventory_accuracy": 91,
        "eta_stability": 82
    }

    dashboard = DigitalTwinDashboard()

    result = dashboard.generate(telemetry)

    print("=" * 60)
    print(" AEON MATRIX AI CONTROL TOWER")
    print("=" * 60)

    print(json.dumps(
        result,
        indent=2
    ))
