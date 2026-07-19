from mother_brain.decision import DecisionEngine
from execution_layer.action_executor import ActionExecutor
from digital_twin.runtime.feedback import DigitalTwinFeedback


decision = DecisionEngine().process(
    "Inventory Re-Sync"
)

execution = ActionExecutor().execute(
    decision
)

twin = DigitalTwinFeedback().update(
    execution
)

print("=== AEON MATRIX AUTONOMOUS EXECUTION ===")
print("DECISION:", decision)
print("EXECUTION:", execution)
print("DIGITAL TWIN:", twin)
