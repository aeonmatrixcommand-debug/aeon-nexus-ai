

class RuntimeLearningDashboard:


    def generate(self,data):

        return {

            "AI Decision Success Rate":
                data["success_rate"],

            "Learning Mode":
                data["learning_status"]

        }
