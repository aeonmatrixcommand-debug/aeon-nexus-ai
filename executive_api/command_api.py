from command_center.kpi_engine import KPIEngine
from command_center.alert_manager import AlertManager
from command_center.executive_view import ExecutiveView


class CommandAPI:

    def status(self):

        kpis = KPIEngine().calculate()

        alerts = AlertManager().evaluate(kpis)

        return ExecutiveView().render(
            kpis,
            alerts
        )
