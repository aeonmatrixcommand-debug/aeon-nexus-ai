def simulate(state, demand_change):

    future_demand = state.demand + demand_change

    risk = 0.1

    if future_demand > state.inventory:
        risk = 0.8

    return {
        "future_demand": future_demand,
        "risk": risk,
        "recommendation":
            "Increase Allocation"
            if risk > 0.5
            else "Maintain"
    }
