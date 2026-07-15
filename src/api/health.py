from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from src.runtime.runtime_registry import registry

app = FastAPI(title="AEON MATRIX Runtime API")

events = []
decisions = []

agents = {
    "inventory_agent": {
        "status": "READY",
        "role": "Inventory Intelligence"
    },
    "route_agent": {
        "status": "READY",
        "role": "Route Optimization"
    },
    "forecast_agent": {
        "status": "READY",
        "role": "Demand Forecast"
    }
}


class Command(BaseModel):
    command: str
    target: str | None = None


class Event(BaseModel):
    event: str
    source: str
    payload: dict = {}


class AgentTask(BaseModel):
    task: str
    input: dict = {}


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
        "metrics": {
            "requests": len(events),
            "agents": len(agents),
            "events": len(events)
        },
        "status": "READY"
    }


@app.get("/agents")
def get_agents():
    return {
        "agents": [
            {
                "name": name,
                **data
            }
            for name, data in agents.items()
        ]
    }


@app.post("/agents/{agent}/execute")
def execute_agent(agent: str, task: AgentTask):

    if agent not in agents:
        return {
            "status": "ERROR",
            "message": "Agent not found"
        }

    decision = {
        "agent": agent,
        "task": task.task,
        "decision": "ANALYZE",
        "confidence": 0.94,
        "action": "EXECUTE",
        "timestamp": datetime.utcnow().isoformat()
    }

    decisions.append(decision)

    return decision


@app.post("/events/publish")
def publish_event(event: Event):

    record = {
        "event": event.event,
        "source": event.source,
        "payload": event.payload,
        "timestamp": datetime.utcnow().isoformat()
    }

    events.append(record)

    return {
        "status": "ACCEPTED",
        "event": record
    }


@app.get("/events")
def get_events():
    return {
        "events": events
    }


@app.get("/events/stream")
def event_stream():
    return {
        "stream": "ACTIVE",
        "events": events
    }


@app.post("/command")
def command(cmd: Command):

    decision = {
        "decision": cmd.command,
        "action": "ANALYZE",
        "status": "READY"
    }

    decisions.append(decision)

    return {
        "command": cmd.command,
        "target": cmd.target,
        "status": "ACCEPTED"
    }


@app.get("/decisions")
def get_decisions():
    return {
        "decisions": decisions
    }
