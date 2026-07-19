from retail_intelligence.demand_forecast import DemandForecastEngine
from retail_intelligence.inventory_optimizer import InventoryOptimizer
from retail_intelligence.retail_brain import RetailBrain


forecast_engine = DemandForecastEngine()
optimizer = InventoryOptimizer()
brain = RetailBrain()


forecast = forecast_engine.forecast(1500)

inventory = optimizer.optimize(forecast)

decision = brain.decide(
    forecast,
    inventory
)


print("=================================")
print(" AEON MATRIX AUTONOMOUS RETAIL BRAIN ")
print("=================================")

print("\nDEMAND FORECAST")
print(forecast)

print("\nINVENTORY OPTIMIZATION")
print(inventory)

print("\nRETAIL AI DECISION")
print(decision)

print("\n=================================")
print(" RETAIL INTELLIGENCE ONLINE ")
print(" Sense > Forecast > Optimize > Act ")
print("=================================")
