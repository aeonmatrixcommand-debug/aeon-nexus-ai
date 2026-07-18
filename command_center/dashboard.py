from telemetry_intelligence.tower import TelemetryTower
from kpi_engine_runtime.kpi import KPIEngine


class CommandCenter:

    def __init__(self):
        self.telemetry = TelemetryTower()
        self.kpi = KPIEngine()


    def status(self):

        return {
            "command_center": "ONLINE",
            "telemetry": self.telemetry.collect(
                "Warehouse DC Live Operation"
            ),
            "kpi": self.kpi.calculate()
        }
