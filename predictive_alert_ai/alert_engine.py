import json
from datetime import datetime


class AnomalyDetector:


    def analyze(self, telemetry):

        risks = []

        score = 0


        temperature = telemetry["temperature"]

        workload = telemetry["workload"]

        latency = telemetry["latency"]


        if temperature > 75:
            score += 35
            risks.append(
                "THERMAL_OVERLOAD"
            )


        if workload > 90:
            score += 30
            risks.append(
                "COMPUTE_SATURATION"
            )


        if latency > 120:
            score += 20
            risks.append(
                "HIGH_INFERENCE_LATENCY"
            )


        if score >=70:
            level="CRITICAL"

        elif score>=40:
            level="WARNING"

        else:
            level="NORMAL"


        return {

            "risk_score":
                score,

            "risk_level":
                level,

            "detected_patterns":
                risks
        }



class GuardianAI:


    def decide(self, risk):

        if risk["risk_level"]=="CRITICAL":

            return {

                "action":
                    "EMERGENCY_OPTIMIZATION",

                "automation":
                    "LOCKED",

                "human_review":
                    True
            }


        elif risk["risk_level"]=="WARNING":

            return {

                "action":
                    "PREVENTIVE_ADJUSTMENT",

                "automation":
                    "ENABLED"
            }


        return {

            "action":
                "CONTINUE_MONITORING",

            "automation":
                "ENABLED"
        }



class IncidentReporter:


    def generate(self, telemetry,risk,response):

        return {

            "incident":
                "AEON MATRIX AI ALERT REPORT",

            "time":
                datetime.utcnow().isoformat(),

            "telemetry":
                telemetry,

            "risk":
                risk,

            "guardian_response":
                response
        }



if __name__=="__main__":


    telemetry = {

        "temperature":82,

        "workload":94,

        "latency":145
    }


    detector = AnomalyDetector()

    risk = detector.analyze(
        telemetry
    )


    response = GuardianAI().decide(
        risk
    )


    report = IncidentReporter().generate(
        telemetry,
        risk,
        response
    )


    print("="*70)
    print(" AEON MATRIX PREDICTIVE ALERT INTELLIGENCE ")
    print("="*70)


    print(
        json.dumps(
            report,
            indent=2
        )
    )

