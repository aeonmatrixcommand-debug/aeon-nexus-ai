<<<<<<< HEAD
from .demand.demand_engine import predict
from .inventory.inventory_optimizer import optimize
from .supplier.supplier_risk import analyze
from .logistics.logistics_adapter import adapt
from .memory.supply_chain_memory import save
=======
from services.guardian.supply_chain_intelligence.demand.demand_engine import predict
from services.guardian.supply_chain_intelligence.inventory.inventory_optimizer import optimize
from services.guardian.supply_chain_intelligence.supplier.supplier_risk import analyze
from services.guardian.supply_chain_intelligence.logistics.logistics_adapter import adapt
from services.guardian.supply_chain_intelligence.memory.supply_chain_memory import save
>>>>>>> origin/main


demand = predict(
    "FAST_MOVING_SKU"
)

inventory = optimize(
    "WAREHOUSE_STOCK"
)

supplier = analyze(
    "SUPPLIER_NETWORK"
)

logistics = adapt(
    "DELIVERY_NETWORK"
)

print(demand)
print(inventory)
print(supplier)
print(logistics)
print(save(logistics))
