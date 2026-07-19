

class LearningEngine:


    def analyze(self, outcomes):

        if not outcomes:

            return {
                "confidence":0,
                "improvement":0
            }


        success_rate = (
            sum(
                1 for x in outcomes
                if x["success"]
            )
            /
            len(outcomes)
        )


        return {

            "success_rate":success_rate,

            "improvement":
                round(success_rate * 100,2),

            "learning_status":
                "ADAPTIVE"

        }
