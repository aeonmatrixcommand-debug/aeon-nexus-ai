from pilot_runtime.health_check import EnterpriseHealthCheck
from pilot_runtime.pilot import PilotRuntime


health = EnterpriseHealthCheck()
pilot = PilotRuntime()


print("=================================")
print(" AEON MATRIX FINAL PILOT RUNTIME ")
print("=================================")

print("\nSYSTEM HEALTH CHECK")
print(
    health.validate()
)

print("\nPILOT LAUNCH")
print(
    pilot.launch()
)

print("\n=================================")
print(" AEON MATRIX ENTERPRISE READY ")
print(" Sense > Think > Decide > Act > Learn ")
print("=================================")
