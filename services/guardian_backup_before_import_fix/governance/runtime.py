class GovernanceControl:
    def validate(self, action: dict) -> dict:
        return {
            "approved": True,
            "action": action
        }
