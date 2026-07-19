from predictive_ops.engine import PredictiveOperationsEngine


engine = PredictiveOperationsEngine()


event = """
Warehouse DC:
Inventory mismatch detected
Order delay increasing
Driver ETA unstable
"""


result = engine.analyze(event)


print("=== AEON MATRIX PREDICTIVE OPERATIONS ===")
print(result)
