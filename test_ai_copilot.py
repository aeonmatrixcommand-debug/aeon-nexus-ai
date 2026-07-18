from ai_gateway.copilot import AICopilot


event = """
Warehouse DC:
Inventory mismatch detected
Order delay increasing
Driver ETA unstable
"""


result = AICopilot().analyze(event)

print("=== AEON MATRIX AI COPILOT ===")
print(result)
