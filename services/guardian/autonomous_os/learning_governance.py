class LearningGovernance:

    def validate(self, learning):

        confidence = learning.get(
            "confidence",
            0
        )

        return {
            "learning_allowed": confidence >= 0.8,
            "confidence": confidence
        }
