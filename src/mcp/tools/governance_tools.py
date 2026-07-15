
def request_approval(payload):

    return {
        "action": payload.get("action"),
        "status": "waiting_for_human_approval",
        "human_in_loop": True
    }


def validate_policy(payload):

    blocked = [
        "delete_inventory",
        "shutdown_operation"
    ]

    action = payload.get("action")

    return {
        "allowed": action not in blocked,
        "action": action
    }
