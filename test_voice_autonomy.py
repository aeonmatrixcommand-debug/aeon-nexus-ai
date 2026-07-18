from ai.voice_hub.command import VoiceCommandHub
from mother_brain.decision import DecisionEngine
from execution_layer.action_executor import ActionExecutor
from digital_twin.runtime.feedback import DigitalTwinFeedback


voice = VoiceCommandHub()

decision_engine = DecisionEngine()

executor = ActionExecutor()

twin = DigitalTwinFeedback()


voice_command = voice.listen(
    "Execute inventory re-sync for warehouse DC"
)


if voice_command["intent"] == "INVENTORY_ANALYSIS":

    decision = decision_engine.process(
        "Inventory Re-Sync"
    )

else:

    decision = decision_engine.process(
        "General Review"
    )


execution = executor.execute(
    decision
)


feedback = twin.update(
    execution
)


print("=== AEON MATRIX AUTONOMOUS VOICE FLOW ===")
print("VOICE:", voice_command)
print("DECISION:", decision)
print("EXECUTION:", execution)
print("DIGITAL TWIN:", feedback)
