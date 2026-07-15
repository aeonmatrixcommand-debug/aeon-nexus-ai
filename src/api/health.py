from fastapi import FastAPI
from pydantic import BaseModel
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

agents = [
    {
        "name": "inventory_agent",
        "status": "READY",
        "role": "Inventory Intelligence"
    },
    {
        "name": "route_agent",
        "status": "READY",
        "role": "Route Optimization"
    },
    {
        "name": "forecast_agent",
        "status": "READY",
        "role": "Demand Forecast"
    },
]

events = []

decisions = []


class CommandRequest(BaseModel):
    command: str
    target: str


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
        "services": registry.status()
    }


@app.get("/metrics")
def metrics():
    return {
        "requests": 0,
        "agents": len(agents),
        "events": len(events),
        "status": "READY"
    }


@app.get("/agents")
def get_agents():
    return {
        "agents": agents
    }


@app.get("/events")
def get_events():
    return {
        "events": events
    }


@app.post("/command")
def command(request: CommandRequest):
    event = {
        "command": request.command,
        "target": request.target,
        "status": "ACCEPTED"
    }

    events.append(event)

    decisions.append({
        "decision": request.command,
        "action": "ANALYZE",
        "status": "READY"
    })

    return event


@app.get("/decisions")
def get_decisions():
    return {
        "decisions": decisions
    }
