from autonomy.execution_engine import ExecutionEngine
from autonomy.feedback_loop import FeedbackLoop


engine = ExecutionEngine()
feedback = FeedbackLoop()


action = "move_to_backup_storage"

result = engine.execute(action)

print("EXECUTION:")
print(result)

print("\nFEEDBACK:")
print(
    feedback.record(
        action,
        result
    )
)
