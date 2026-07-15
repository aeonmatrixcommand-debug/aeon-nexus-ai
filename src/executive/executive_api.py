from executive.kpi_engine import KPIEngine


class ExecutiveAPI:

    def __init__(self):

        self.kpi = KPIEngine()


    def dashboard(self):

        return {

            "system":
            "AEON_MATRIX_EXECUTIVE_COMMAND_CENTER",


            "dashboard_status":
            "operational",


            "kpis":
            self.kpi.calculate(),


            "decision_ready":
            True

        }
