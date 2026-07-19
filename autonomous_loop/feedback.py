from datetime import datetime


class LearningFeedback:

    def record(self, decision, result):

        return {
            "learning_status": "UPDATED",
            "decision": decision,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        }
