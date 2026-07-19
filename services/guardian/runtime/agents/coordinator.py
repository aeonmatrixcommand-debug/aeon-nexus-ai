from services.guardian.runtime.agents.task_router import route_task


def coordinate(context):

    task = context.get("task")

    allocation = route_task(task)

    return {
        "agent_plan": allocation,
        "decision": "EXECUTE",
        "confidence": 0.9
    }
