from mother_brain.runtime import MotherBrain


brain = MotherBrain()


result = brain.analyze(
"""
Warehouse DC:

- Order delay increasing
- Inventory mismatch detected
- Driver ETA unstable

"""
)

print(result)
