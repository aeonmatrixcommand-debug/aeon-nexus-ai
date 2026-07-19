from .asset.asset_registry import register
from .health.health_predictor import predict
from .planning.maintenance_planner import schedule
from .risk.failure_risk import analyze
from .memory.asset_memory import save


asset = register(
    "WAREHOUSE_CONVEYOR_01",
    "LOGISTICS_EQUIPMENT"
)

health = predict(
    asset
)

maintenance = schedule(
    health
)

risk = analyze(
    health
)

print(asset)
print(health)
print(maintenance)
print(risk)
print(save(risk))
