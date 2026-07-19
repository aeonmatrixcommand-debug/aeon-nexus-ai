class DashboardEngine:
    """
    Generate adaptive dashboard from Digital Twin state.
    Human-AI shared understanding layer.
    """

    def generate(self, twin_state):

        dashboard = {
            "situation": "normal",
            "risk_summary": [],
            "impact_summary": {},
            "opportunities": [],
            "recommended_actions": []
        }

        if hasattr(twin_state, "risks"):

            for risk in twin_state.risks:

                dashboard["risk_summary"].append({
                    "type": risk.get("type"),
                    "severity": risk.get("severity", "unknown"),
                    "reason": risk.get("reason", "detected by AI")
                })


        if hasattr(twin_state, "impacts"):
            dashboard["impact_summary"] = twin_state.impacts


        if len(dashboard["risk_summary"]) > 0:

            dashboard["situation"] = "attention_required"

            dashboard["recommended_actions"].append(
                "Review AI detected risks and execute mitigation plan"
            )


        return dashboard
