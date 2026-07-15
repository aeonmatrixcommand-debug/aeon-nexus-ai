class ApprovalEngine:
    """
    Human in the loop approval.
    """

    def request(self, action):

        return {
            "action": action,
            "status": "waiting_for_approval",
            "human_required": True
        }


    def approve(self, action):

        return {
            "action": action,
            "status": "approved",
            "human_required": True
        }
