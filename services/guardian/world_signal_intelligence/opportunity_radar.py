class OpportunityRadar:

    def detect(self, intelligence):

        if intelligence["status"] == "OPPORTUNITY":

            return {
                "opportunity": True,
                "action": "EXPAND_CAPACITY",
                "confidence": intelligence["signal_score"]
            }

        return {
            "opportunity": False,
            "action": "MONITOR",
            "confidence": intelligence["signal_score"]
        }
