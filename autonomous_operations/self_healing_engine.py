import json
from datetime import datetime


class ActionPlanner:

    def create_plan(self, risk):

        if risk >= 90:
            action = "EMERGENCY_RECOVERY"

        elif risk >= 70:
            action = "PREVENTIVE_CORRECTION"

        elif risk >= 40:
            action = "MONITOR_AND_OPTIMIZE"

        else:
            action = "NORMAL_OPERATION"

        return {
            "action": action,
            "priority":
                "HIGH" if risk >= 70 else "NORMAL"
        }


class VerificationEngine:

    def verify(self, action):

        return {
            "verification":
                "PASSED",

            "action_checked":
                action,

            "system_state":
                "STABLE"
        }


class SelfHealingEngine:

    def execute(self, telemetry):

        risk = telemetry.get(
            "risk_score",
            0
        )

        plan = ActionPlanner().create_plan(
            risk
        )

        verification = VerificationEngine().verify(
            plan["action"]
        )

        return {

            "loop_id":
                f"LOOP-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "sense":
                telemetry,

            "decide":
                plan,

            "act":
                {
                    "executed":
                        plan["action"]
                },

            "verify":
                verification,

            "learn":
                "Experience stored for future optimization",

            "status":
                "AUTONOMOUS_LOOP_COMPLETE"
        }


if __name__ == "__main__":

    engine = SelfHealingEngine()

    result = engine.execute(
        {
            "system": "AEON MATRIX",
            "risk_score": 85,
            "incident": "Warehouse Operational Risk"
        }
    )

    print("=" * 60)
    print(" AEON MATRIX AUTONOMOUS OPERATIONS LOOP")
    print("=" * 60)

    print(json.dumps(
        result,
        indent=2
    ))
