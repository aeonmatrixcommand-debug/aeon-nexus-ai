def run_scenario(state, scenarios):

    results = []

    for value in scenarios:
        results.append({
            "change": value,
            "demand":
                state.demand + value
        })

    return results
