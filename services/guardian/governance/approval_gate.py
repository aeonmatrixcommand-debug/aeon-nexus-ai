class ApprovalGate:

    def request(self, policy_result):

        if policy_result["status"] == "REVIEW":
            return {
                "approved": False,
                "human_required": True
            }

        return {
            "approved": policy_result["status"] == "APPROVED",
            "human_required": False
        }
