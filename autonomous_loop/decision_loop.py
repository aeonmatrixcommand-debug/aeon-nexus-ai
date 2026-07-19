from datetime import datetime


class AutonomousDecisionLoop:

    def run(self, event, risk):

        decision = "EXECUTE" if risk < 70 else "HUMAN_APPROVAL"

        return {
            "event": event,
            "risk_score": risk,
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        }
