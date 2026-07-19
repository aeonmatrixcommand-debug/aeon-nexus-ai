def evaluate_agent(result):

    return {
        "agent": result["agent_plan"]["assigned_agent"],
        "performance": 1.0,
        "confidence": result["confidence"]
    }
