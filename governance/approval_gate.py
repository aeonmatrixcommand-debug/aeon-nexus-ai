
class ApprovalGate:


    def check(self,action):

        return {

            "action":

            action,


            "approval":

            "REQUIRED",


            "human_in_loop":

            True

        }

