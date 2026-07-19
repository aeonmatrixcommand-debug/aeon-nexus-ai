def build_workflow(event):

    return {
        "trigger": event,
        "steps": [
            "Analyze",
            "Decide",
            "Execute",
            "Learn"
        ]
    }
