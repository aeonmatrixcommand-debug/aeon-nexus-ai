

class OptimizationEngine:


    def optimize(
        self,
        inventory,
        demand,
        capacity
    ):


        utilization = (
            demand / capacity
        )


        if utilization > 0.9:

            action="INCREASE_CAPACITY"

        elif inventory > demand:

            action="REDUCE_ALLOCATION"

        else:

            action="BALANCE_FLOW"



        return {

            "action":action,

            "utilization":
                round(utilization,2)

        }
