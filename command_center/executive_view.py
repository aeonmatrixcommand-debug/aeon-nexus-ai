class ExecutiveView:

    def render(self, kpis, alerts):

        return {
            "dashboard": "AEON MATRIX COMMAND CENTER",
            "kpi": kpis,
            "alerts": alerts,
            "status": "ONLINE"
        }
