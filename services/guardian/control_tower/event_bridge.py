def create_event(decision):

    return {
        "topic": "guardian.control.decision",
        "decision": decision["decision"],
        "confidence": decision["confidence"]
    }
