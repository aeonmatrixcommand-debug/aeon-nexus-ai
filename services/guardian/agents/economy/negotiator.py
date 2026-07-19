from services.guardian.agents.economy.capability_registry import registry


def negotiate(skill):

    agents = registry.find(skill)

    if not agents:
        return None

    winner = max(
        agents,
        key=lambda x: x.confidence
    )

    return {
        "selected_agent": winner.name,
        "confidence": winner.confidence,
        "cost": winner.cost,
        "sla": winner.sla
    }
