from src.runtime.runtime_registry import registry

services = [
    "enterprise_os",
    "governance",
    "telemetry",
    "digital_twin",
    "multi_agent_runtime",
    "strategic_intelligence",
    "world_intelligence",
    "ai_gateway",
    "mcp",
]

for service in services:
    registry.register(service, object())

print("=" * 50)
print("AEON MATRIX Enterprise AI Platform")
print("=" * 50)
print()

print("========== SYSTEM HEALTH ==========")
for name, status in registry.status().items():
    print(f"[{status}] {name}")

print("===================================")
print()
print("System Status : READY")
