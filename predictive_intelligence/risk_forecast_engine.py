import json
from datetime import datetime


class RiskForecastEngine:

    def __init__(self, simulation_result):
        self.simulation = simulation_result

    def forecast(self):

        analysis = self.simulation.get("analysis", {})
        risk_score = analysis.get("risk_score", 0)

        if risk_score >= 90:
            forecast = "FAILURE_IMMINENT"
            window = "0-30 MINUTES"

        elif risk_score >= 70:
            forecast = "HIGH_RISK_ESCALATION"
            window = "30-120 MINUTES"

        elif risk_score >= 40:
            forecast = "MONITOR_REQUIRED"
            window = "2-24 HOURS"

        else:
            forecast = "STABLE"
            window = "24+ HOURS"

        return {
            "forecast_id":
                f"RF-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "risk_score":
                risk_score,

            "prediction":
                forecast,

            "time_window":
                window,

            "recommended_action": (
                "IMMEDIATE_ESCALATION"
                if risk_score >= 70
                else "CONTINUE_MONITORING"
            ),

            "generated_at":
                datetime.utcnow().isoformat()
        }


if __name__ == "__main__":

    simulation = {
        "analysis": {
            "risk_score": 100
        }
    }

    engine = RiskForecastEngine(simulation)

    print("=" * 45)
    print(" AEON MATRIX PREDICTIVE INTELLIGENCE")
    print("=" * 45)

    print(json.dumps(
        engine.forecast(),
        indent=2
    ))
