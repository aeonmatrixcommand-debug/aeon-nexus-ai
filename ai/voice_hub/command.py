class VoiceCommandHub:

    def listen(self, voice_input):

        return {
            "input": voice_input,
            "intent": self.detect_intent(voice_input)
        }


    def detect_intent(self, text):

        text = text.lower()

        if "inventory" in text:
            return "INVENTORY_ANALYSIS"

        if "route" in text:
            return "ROUTE_CONTROL"

        if "risk" in text:
            return "RISK_ANALYSIS"

        return "GENERAL_QUERY"


    def respond(self, command):

        return {
            "voice_response":
                f"AEON MATRIX executing {command['intent']}",
            "status": "READY"
        }
