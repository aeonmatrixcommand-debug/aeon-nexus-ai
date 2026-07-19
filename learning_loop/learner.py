class LearningEngine:

    def learn(self, result):

        return {
            "learning_status": "UPDATED",
            "feedback": result,
            "model_action": "ADJUST_PARAMETERS"
        }
