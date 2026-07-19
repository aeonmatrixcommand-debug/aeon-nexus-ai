class ExecutiveView:
    """
    Convert Digital Twin intelligence into executive decision view.
    """

    def generate(self, situation, insight, impact=None):

        view = {
            "status": situation["status"],
            "title": situation["title"],
            "executive_summary": "",
            "business_impact": impact or {},
            "key_insights": insight,
            "decision_required": [],
            "confidence": 0.0
        }

        if situation["status"] == "attention_required":

            view["executive_summary"] = (
                "Operational risk detected. "
                "Management attention is required."
            )

            view["decision_required"].append(
                "Review mitigation action"
            )

            view["confidence"] = 0.90

        else:

            view["executive_summary"] = (
                "Operations are stable."
            )

            view["confidence"] = 0.95

        return view
