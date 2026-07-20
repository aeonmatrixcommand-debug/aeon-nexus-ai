from services.guardian.control_tower.signal import RuntimeSignal


def analyze_signal(signal: RuntimeSignal):

    if signal.severity == "HIGH":
        decision = "ESCALATE"

    else:
        decision = "OPTIMIZE"

    return {
        "decision": decision,
        "source": signal.source,
        "confidence": 0.92
    }
