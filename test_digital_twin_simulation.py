from simulation_engine.digital_twin_simulator import DigitalTwinSimulator
from simulation_engine.scenario_planner import ScenarioPlanner


twin = DigitalTwinSimulator()
planner = ScenarioPlanner()


print("=================================")
print(" AEON MATRIX DIGITAL TWIN AI ")
print("=================================")


simulation = twin.simulate(
    "WAREHOUSE_AND_FLEET_OPTIMIZATION"
)


print("\nDIGITAL TWIN SIMULATION")
print(simulation)


print("\nSCENARIO DECISION")
print(
    planner.analyze(simulation)
)


print("\n=================================")
print(" PREDICTIVE ENTERPRISE CONTROL ONLINE ")
print(" Sense > Simulate > Predict > Act ")
print("=================================")
