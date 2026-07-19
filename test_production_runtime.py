from api_gateway.server import APIGateway
from production_runtime.health import SystemHealth


api = APIGateway()
health = SystemHealth()


print("=== AEON MATRIX PRODUCTION RUNTIME ===")

print("\nAPI GATEWAY")
print(api.health())

print("\nSYSTEM HEALTH")
print(health.check())

print("\nCOMMAND TEST")
print(
    api.execute(
        "OPTIMIZE_WAREHOUSE_FLOW"
    )
)
