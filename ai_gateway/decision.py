class DecisionContract:


    def build(
        self,
        analysis,
        guardian
    ):

        return {

            "analysis": analysis,

            "guardian":
                guardian,

            "status":
                "DECISION_READY"

        }
