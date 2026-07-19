import json
from datetime import datetime


class VoiceCommandParser:


    def parse(self, command):

        command = command.lower()


        if "risk" in command:
            intent = "RISK_ANALYSIS"

        elif "inventory" in command:
            intent = "INVENTORY_STATUS"

        elif "delivery" in command or "eta" in command:
            intent = "DELIVERY_INTELLIGENCE"

        else:
            intent = "GENERAL_EXECUTIVE_QUERY"


        return {

            "original_command":
                command,

            "intent":
                intent
        }



class ExecutiveAI:


    def answer(self, intent):

        responses = {


            "RISK_ANALYSIS":
                "Current operational risk is LOW. Guardian AI monitoring active.",


            "INVENTORY_STATUS":
                "Inventory accuracy is 97.8%. No critical mismatch detected.",


            "DELIVERY_INTELLIGENCE":
                "ETA prediction confidence is 94.5%. Delivery network stable.",


            "GENERAL_EXECUTIVE_QUERY":
                "AEON MATRIX is operating in autonomous optimization mode."
        }


        return {

            "response":
                responses[intent],

            "confidence":
                96
        }



class DecisionRouter:


    def route(self, intent):

        return {

            "action":
                "ANALYZE_AND_REPORT",

            "governance":
                "APPROVAL_POLICY_CHECKED",

            "intent":
                intent
        }



class AuditLogger:


    def save(self, command, result):

        return {

            "audit":
                "RECORDED",

            "time":
                datetime.utcnow().isoformat(),

            "command":
                command,

            "result":
                result
        }



if __name__ == "__main__":


    command = (
        "Show me current inventory risk status"
    )


    parsed = VoiceCommandParser().parse(
        command
    )


    answer = ExecutiveAI().answer(
        parsed["intent"]
    )


    decision = DecisionRouter().route(
        parsed["intent"]
    )


    audit = AuditLogger().save(
        command,
        answer
    )


    report = {

        "system":
            "AEON MATRIX VOICE EXECUTIVE COPILOT",

        "timestamp":
            datetime.utcnow().isoformat(),

        "command":
            parsed,

        "ai_answer":
            answer,

        "decision":
            decision,

        "audit":
            audit
    }


    print("="*70)
    print(
        " AEON MATRIX VOICE EXECUTIVE COPILOT "
    )
    print("="*70)

    print(
        json.dumps(
            report,
            indent=2
        )
    )

