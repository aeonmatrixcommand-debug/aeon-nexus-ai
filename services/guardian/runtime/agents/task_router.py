from services.guardian.agents.registry import registry


def route_task(task):

    for agent, info in registry.list_agents().items():

        if info["capability"] in task:
            return {
                "task": task,
                "assigned_agent": agent,
                "status": "ALLOCATED"
            }

    return {
        "task": task,
        "assigned_agent": "General Agent",
        "status": "FALLBACK"
    }
