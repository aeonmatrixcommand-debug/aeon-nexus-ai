from logistics_intelligence.event_bus import EventBus
from logistics_intelligence.eta_engine import ETAPredictionEngine
from logistics_intelligence.optimizer import LogisticsOptimizer


bus = EventBus()
eta_engine = ETAPredictionEngine()
optimizer = LogisticsOptimizer()


event = bus.publish(
    "DELIVERY_UPDATE",
    {
        "vehicle": "TRUCK-001",
        "location": "DC-A"
    }
)


eta = eta_engine.predict(
    distance=40,
    traffic=1
)


decision = optimizer.optimize(eta)


print("=================================")
print(" AEON MATRIX LOGISTICS INTELLIGENCE ")
print("=================================")

print("\nEVENT BUS")
print(event)

print("\nETA PREDICTION")
print(eta)

print("\nAUTONOMOUS OPTIMIZATION")
print(decision)

print("\n=================================")
print(" LOGISTICS AI ONLINE ")
print(" Sense > Predict > Optimize > Execute ")
print("=================================")
