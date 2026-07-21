

signal = collect(
    "GLOBAL_MARKET",
    "AI_SUPPLY_CHAIN_TRANSFORMATION"
)

trend = analyze(
    signal
)

risk = detect(
    trend
)

opportunity = identify(
    signal
)

print(signal)
print(trend)
print(risk)
print(opportunity)
print(save(opportunity))
