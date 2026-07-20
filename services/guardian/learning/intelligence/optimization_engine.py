def optimize(pattern):
    if pattern["confidence"] >= 0.8:
        return {
            "action": "increase_trust",
            "confidence": pattern["confidence"]
        }

    return {
        "action": "review_policy",
        "confidence": pattern["confidence"]
    }
