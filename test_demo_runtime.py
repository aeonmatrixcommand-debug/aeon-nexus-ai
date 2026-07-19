from demo_runtime.live_command_center import LiveCommandCenter


center = LiveCommandCenter()


print("=================================")
print(" AEON MATRIX LIVE COMMAND CENTER ")
print("=================================")

print("\nSYSTEM STATUS")
print(center.run())

print("\nEXECUTIVE KPI WALL")
print(center.kpi())

print("\nAI WORKFORCE STATUS")
for agent in center.agents():
    print("-", agent)

print("\n=================================")
print(" AEON MATRIX ENTERPRISE DEMO READY ")
print(" Sense > Think > Decide > Act > Learn ")
print("=================================")
