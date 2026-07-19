class CausalEngine:
    """
    Analyze cause-effect relationship.
    """

    def analyze(self, event):

        if event == "cold_chain_breach":

            return {
                "cause":
                    "Temperature control failure",

                "impact_chain":[
                    "Temperature increase",
                    "Shelf life reduction",
                    "Customer SLA risk",
                    "Financial loss"
                ]
            }


        return {
            "cause":"Unknown",
            "impact_chain":[]
        }


    # Compatibility alias
    def analyse(self, event):
        return self.analyze(event)
