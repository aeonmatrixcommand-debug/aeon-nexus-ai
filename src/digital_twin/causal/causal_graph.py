class CausalGraph:

    def analyze(self, event):

        graph = {
            "event": event,
            "cause": None,
            "impact": None,
            "opportunity": None
        }

        if event == "cold_chain_breach":

            graph["cause"] = "temperature instability"
            graph["impact"] = "product quality risk"
            graph["opportunity"] = "optimize cold chain monitoring"

        return graph


    # compatibility layer
    def analyse(self, event):

        return self.analyze(event)
