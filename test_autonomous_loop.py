from autonomous_loop.decision_loop import AutonomousDecisionLoop
from autonomous_loop.feedback import LearningFeedback
from autonomous_loop.audit import AIAuditTrail


brain = AutonomousDecisionLoop()
learn = LearningFeedback()
audit = AIAuditTrail()


event = """
Warehouse DC:
Inventory mismatch
Order delay
ETA unstable
"""


decision = brain.run(
    event,
    45
)

print("=== AEON MATRIX AUTONOMOUS LOOP ===")

print("\nDECISION")
print(decision)

print("\nAUDIT")
print(
    audit.log(
        "Inventory Recovery Execution"
    )
)

print("\nLEARNING")
print(
    learn.record(
        decision,
        "SUCCESS"
    )
)
