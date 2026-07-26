
class RollbackEngine:


    def rollback(self, action):

        return {
            "rollback":True,
            "action":action,
            "status":"READY"
        }
