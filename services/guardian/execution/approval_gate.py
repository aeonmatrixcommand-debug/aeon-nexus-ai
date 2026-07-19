class ApprovalGate:

    def approve(self, decision):

        confidence = decision.get(
            "confidence",
            0
        )

        return {
            "approved": confidence >= 0.8,
            "reason": (
                "AUTO_APPROVED"
                if confidence >= 0.8
                else "HUMAN_REVIEW_REQUIRED"
            )
        }
