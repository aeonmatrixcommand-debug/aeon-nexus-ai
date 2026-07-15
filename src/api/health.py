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

runtime_metrics = {
    "requests": 0,
    "agents": 0,
    "events": 0,
}


@app.on_event("startup")
def startup():
    for service in SERVICES:
        registry.register(service, object())


@app.middleware("http")
async def count_requests(request, call_next):
    runtime_metrics["requests"] += 1
    response = await call_next(request)
    return response


@app.get("/health")
def health():
    return {
        "status": "READY",
        "services": registry.status()
    }


@app.get("/ready")
def ready():
    return {
        "ready": True,
        "status": "READY"
    }


@app.get("/version")
def version():
    return {
        "platform": "AEON MATRIX",
        "runtime": "Integration Sprint",
        "version": "1.0.0"
    }


@app.get("/runtime")
def runtime():
    return {
        "platform": "AEON MATRIX",
        "runtime": "ACTIVE",
        "components": [
            "AI Gateway",
            "MCP",
            "Digital Twin",
            "Telemetry",
            "Multi-Agent Runtime"
        ],
        "services": registry.status()
    }


@app.get("/metrics")
def metrics():
    return {
        "metrics": runtime_metrics,
        "status": "READY"
    }
