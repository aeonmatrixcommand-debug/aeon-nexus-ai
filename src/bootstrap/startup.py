from bootstrap.service_registry import ServiceRegistry
from bootstrap.health import HealthCheck

def startup():
    registry = ServiceRegistry()

    services = [
        "Enterprise OS",
        "Governance",
        "Telemetry",
        "Digital Twin",
        "Multi-Agent Runtime",
        "Strategic Intelligence",
        "World Intelligence",
        "AI Gateway",
        "MCP"
    ]

    for service in services:
        registry.register(service)

    HealthCheck.report(registry)
    return registry
