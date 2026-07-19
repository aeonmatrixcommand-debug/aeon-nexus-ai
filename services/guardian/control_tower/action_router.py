def route_action(decision):

    return {
        "action": decision["decision"],
        "agent": "Autonomous Agent",
        "status": "READY",
        "confidence": decision["confidence"]
    }
