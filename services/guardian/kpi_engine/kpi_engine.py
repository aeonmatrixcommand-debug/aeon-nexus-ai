class KPIEngine:
    def calculate(self, metrics: dict) -> dict:
        return {
            "otif": metrics.get("otif"),
            "sla": metrics.get("sla"),
            "inventory_accuracy": metrics.get("inventory_accuracy"),
            "fleet_utilization": metrics.get("fleet_utilization"),
            "eta_accuracy": metrics.get("eta_accuracy"),
        }
