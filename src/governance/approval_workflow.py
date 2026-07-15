class ApprovalWorkflow:
    """
    Human-in-the-loop control.
    """


    def request(self, action, risk):

        return {
            "action": action,
            "risk": risk,
            "status": "waiting_for_human_review"
        }


    def approve(self, action):

        return {
            "action": action,
            "status": "approved",
            "approved_by": "human_controller"
        }
