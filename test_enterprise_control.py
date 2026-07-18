from digital_twin.runtime import DigitalTwin
from command_center.runtime import CommandCenter
from kpi_engine.monitor import KPIEngine


twin = DigitalTwin()
center = CommandCenter()
kpi = KPIEngine()


print("=== AEON MATRIX ENTERPRISE CONTROL CENTER ===")

print("\nDIGITAL TWIN")
print(
    twin.sync(
        "Warehouse DC Operation"
    )
)

print("\nCOMMAND CENTER")
print(
    center.monitor(
        "Inventory + Transport Telemetry"
    )
)

print("\nKPI INTELLIGENCE")
print(
    kpi.calculate()
)
