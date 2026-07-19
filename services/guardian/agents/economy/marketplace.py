from services.guardian.agents.economy.capability_registry import registry


def publish_task(task):

    agents = registry.find(
        task["skill"]
    )

    return {
        "task": task["name"],
        "candidates": [
            a.name for a in agents
        ]
    }
