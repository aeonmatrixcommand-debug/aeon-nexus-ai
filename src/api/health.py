from fastapi import FastAPI
from src.runtime.runtime_registry import registry

app = FastAPI(title="AEON MATRIX Runtime API")

SERVICES = [
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

@app.on_event("startup")
def startup():
    for service in SERVICES:
        registry.register(service, object())

@app.get("/health")
def health():
    return {
        "status": "READY",
        "services": registry.status()
    }

@app.get("/ready")
def ready():
    return {"ready": True}

@app.get("/version")
def version():
    return {
        "platform": "AEON MATRIX",
        "runtime": "Integration Sprint"
    }

@app.get("/runtime")
def runtime():
    services = registry.status()
    return {
        "platform": "AEON MATRIX",
        "runtime": {
            "mode": "AUTONOMOUS",
            "services": len(services),
            "status": "READY"
        },
        "services": services
    }


@app.get("/metrics")
def metrics():
    services = registry.status()
    return {
        "platform": "AEON MATRIX",
        "metrics": {
            "service_count": len(services),
            "health_score": 100 if services else 0,
            "status": "READY"
        }
    }
