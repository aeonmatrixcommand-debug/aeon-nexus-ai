from executive_intelligence.kpi_engine import KPIEngine
from executive_intelligence.business_simulator import BusinessImpactSimulator
from executive_intelligence.command_center import ExecutiveCommandCenter


kpi = KPIEngine()
simulator = BusinessImpactSimulator()
center = ExecutiveCommandCenter()


print("=================================")
print(" AEON MATRIX EXECUTIVE COMMAND CENTER ")
print("=================================")

print("\nSYSTEM STATUS")
print(center.status())

print("\nENTERPRISE KPI")
print(kpi.calculate())

print("\nBUSINESS IMPACT SIMULATION")
print(
    simulator.simulate(
        "OPTIMIZE_LOGISTICS_NETWORK"
    )
)

print("\n=================================")
print(" EXECUTIVE INTELLIGENCE ONLINE ")
print(" Sense > Decide > Execute > Measure ")
print("=================================")
