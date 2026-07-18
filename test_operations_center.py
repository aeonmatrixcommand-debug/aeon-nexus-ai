from telemetry_intelligence.collector import TelemetryCollector
from observability_center.monitor import OperationsMonitor


collector = TelemetryCollector()
monitor = OperationsMonitor()


telemetry = collector.collect(
    "AEON-MATRIX-WMS",
    {
        "OTIF": 96.8,
        "Inventory_Accuracy": 99.1,
        "ETA_Risk": 12
    }
)


print("=== AEON MATRIX AI OPERATIONS CENTER ===")

print("\nTELEMETRY STREAM")
print(telemetry)

print("\nSYSTEM OBSERVABILITY")
print(
    monitor.analyze(telemetry)
)
