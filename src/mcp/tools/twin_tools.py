from datetime import datetime


def get_twin_state(payload):
    return {
        "entity": payload.get("entity", "unknown"),
        "state": "operational",
        "timestamp": datetime.utcnow().isoformat()
    }


def simulate_risk(payload):
    risk = payload.get("risk")

    return {
        "risk": risk,
        "simulation": "completed",
        "impact_score": 0.82
    }
