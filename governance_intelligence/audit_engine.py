import json
from datetime import datetime


class GovernancePolicyEngine:

    def evaluate(self, decision):

        risk = decision.get("risk_score", 0)
        action = decision.get("decision", {}).get("action")

        policies = []

        if risk >= 90:
            policies.append("CRITICAL_RISK_REQUIRES_HUMAN_APPROVAL")

        if action == "EMERGENCY_ESCALATION":
            policies.append("EMERGENCY_RESPONSE_PROTOCOL")

        policies.append("AI_DECISION_AUDIT_REQUIRED")

        return {
            "policy_status": "COMPLIANT",
            "rules_checked": policies
        }


class ExplainableAuditEngine:

    def create_record(self, decision, governance):

        return {
            "audit_id":
                f"AUDIT-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "timestamp":
                datetime.utcnow().isoformat(),

            "input":
                {
                    "risk_score":
                        decision.get("risk_score"),

                    "prediction":
                        decision.get("prediction")
                },

            "decision":
                decision.get("decision"),

            "governance":
                governance,

            "explanation":
                "Decision generated from predictive risk analysis with governance validation."
        }


if __name__ == "__main__":

    decision = {
        "risk_score": 100,
        "prediction": "FAILURE_IMMINENT",
        "decision": {
            "action": "EMERGENCY_ESCALATION"
        }
    }

    policy = GovernancePolicyEngine()

    governance = policy.evaluate(decision)

    audit = ExplainableAuditEngine().create_record(
        decision,
        governance
    )

    print("=" * 55)
    print(" AEON MATRIX GOVERNANCE INTELLIGENCE")
    print("=" * 55)

    print(json.dumps(
        audit,
        indent=2
    ))
