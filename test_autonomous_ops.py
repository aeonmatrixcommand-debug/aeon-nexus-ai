from telemetry_bus.event_stream import TelemetryStream
from autonomous_ops.agent import AutonomousOperationsAgent


telemetry = TelemetryStream()
agent = AutonomousOperationsAgent()


event = """
Warehouse DC:
Inventory mismatch detected
Order delay increasing
Driver ETA unstable
"""


signal = telemetry.publish(event)

result = agent.process(event)


print("=== AEON MATRIX AUTONOMOUS OPERATIONS ===")
print("TELEMETRY:")
print(signal)

print("\nAGENT DECISION:")
print(result)
