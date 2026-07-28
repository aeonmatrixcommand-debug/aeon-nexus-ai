class PolicyManager:

    def validate(self, action):
        return {
            "action": action,
            "approved": True
        }
