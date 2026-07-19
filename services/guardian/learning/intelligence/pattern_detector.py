def detect_pattern(events):
    if not events:
        return {"pattern": "none", "confidence": 0}

    success = sum(
        1 for e in events if e.get("outcome") == "SUCCESS"
    )

    confidence = success / len(events)

    return {
        "pattern": "decision_success_pattern",
        "confidence": round(confidence, 2),
    }
