from multi_agent_runtime.agents import AgentRegistry
from multi_agent_runtime.orchestrator import AgentOrchestrator


registry = AgentRegistry()
orchestrator = AgentOrchestrator()


print("=================================")
print(" AEON MATRIX MULTI-AGENT SYSTEM ")
print("=================================")


print("\nACTIVE AI WORKFORCE")

for agent in registry.list_agents():
    print(agent)


print("\nAUTONOMOUS TASK EXECUTION")

print(
    orchestrator.execute(
        "OPTIMIZE_ENTERPRISE_LOGISTICS"
    )
)


print("\n=================================")
print(" MULTI-AGENT OPERATIONS ONLINE ")
print(" Sense > Think > Coordinate > Act ")
print("=================================")
