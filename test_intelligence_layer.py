from intelligence.demand_forecast import DemandForecastEngine
from intelligence.eta_prediction import ETAPredictionEngine
from intelligence.value_recovery import ValueRecoveryEngine


forecast = DemandForecastEngine()
eta = ETAPredictionEngine()
recovery = ValueRecoveryEngine()


print("=== AEON MATRIX INTELLIGENCE LAYER ===")

print("\nDEMAND FORECAST")
print(
    forecast.predict(
        "SKU-001",
        [100,120,110,130,140]
    )
)

print("\nETA PREDICTION")
print(
    eta.predict(
        "DC-BKK-ROUTE-01"
    )
)

print("\nVALUE RECOVERY")
print(
    recovery.analyze(
        2
    )
)
