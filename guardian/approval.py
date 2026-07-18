class ApprovalManager:

    def request(self, decision):

        if decision["decision"] == "AUTO_EXECUTE":
            return "AUTHORIZED"

        if decision["decision"] == "REQUIRES_APPROVAL":
            return "WAITING_HUMAN_APPROVAL"

        return "BLOCKED_PENDING_REVIEW"
