from dataclasses import dataclass


@dataclass
class TwinState:
    warehouse: object
    inventory: object
    demand: object
    risk: object


def update(entity, status):
    return {
        "entity": entity,
        "state": status,
        "status": "UPDATED"
    }
