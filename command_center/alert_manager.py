class AlertManager:

    def evaluate(self, kpis):

        alerts = []

        if kpis["SLA_RISK"] != "LOW":
            alerts.append("SLA RISK DETECTED")

        if float(kpis["INVENTORY_HEALTH"].replace("%","")) < 90:
            alerts.append("INVENTORY HEALTH WARNING")

        if not alerts:
            alerts.append("SYSTEM HEALTHY")

        return alerts
