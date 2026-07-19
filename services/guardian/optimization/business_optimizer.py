

class BusinessOptimizer:


    def evaluate(
        self,
        sla,
        cost
    ):


        score = (
            sla * 0.7
            -
            cost * 0.3
        )


        return {

            "optimization_score":
                round(score,2),

            "status":
                "OPTIMAL"
                if score > 0.7
                else
                "REVIEW"

        }
