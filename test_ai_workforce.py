from agent_marketplace.registry import AgentRegistry
from ai_workforce.orchestrator import AIWorkforce


registry = AgentRegistry()
workforce = AIWorkforce()


registry.register(
    "Inventory Agent",
    "Inventory Optimization"
)

registry.register(
    "ETA Agent",
    "Transport Prediction"
)

registry.register(
    "Risk Agent",
    "Operational Risk Detection"
)


print("=== AEON MATRIX AI WORKFORCE ONLINE ===")

print("\nAGENT MARKETPLACE")
print(
    registry.list_agents()
)

print("\nMULTI AGENT COLLABORATION")
print(
    workforce.assign(
        "Optimize DC Operations",
        registry.list_agents()
    )
)
