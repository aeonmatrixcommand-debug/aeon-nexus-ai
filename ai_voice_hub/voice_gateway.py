import json
from datetime import datetime


class VoiceIntentEngine:

    def process(self, voice_input):

        text = voice_input.lower()

        if "inventory" in text:
            intent = "INVENTORY_STATUS"

        elif "risk" in text or "alert" in text:
            intent = "RISK_MONITORING"

        elif "delivery" in text or "eta" in text:
            intent = "TRANSPORT_STATUS"

        elif "report" in text:
            intent = "EXECUTIVE_BRIEFING"

        else:
            intent = "GENERAL_ASSISTANCE"

        return {
            "recognized_text": voice_input,
            "intent": intent,
            "confidence": 0.96
        }


class ExecutiveAssistant:

    def respond(self, intent):

        responses = {

            "INVENTORY_STATUS":
                "Inventory intelligence report ready.",

            "RISK_MONITORING":
                "Guardian risk monitoring activated.",

            "TRANSPORT_STATUS":
                "ETA and route intelligence analysis started.",

            "EXECUTIVE_BRIEFING":
                "Executive briefing generation initiated.",

            "GENERAL_ASSISTANCE":
                "Command received and routed."
        }

        return responses.get(
            intent,
            "Command processed."
        )


class VoiceHub:

    def execute(self, voice_command):

        intent = VoiceIntentEngine().process(
            voice_command
        )

        response = ExecutiveAssistant().respond(
            intent["intent"]
        )

        return {
            "voice_session_id":
                f"VOICE-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "input":
                voice_command,

            "intent":
                intent,

            "assistant_response":
                response,

            "status":
                "ONLINE"
        }


if __name__ == "__main__":

    hub = VoiceHub()

    result = hub.execute(
        "Show inventory risk and prepare executive report"
    )

    print("=" * 60)
    print(" AEON MATRIX AI VOICE HUB")
    print("=" * 60)

    print(json.dumps(
        result,
        indent=2
    ))
