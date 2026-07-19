class SituationEngine:
    """
    Convert AI detected conditions into human understandable situations.
    """

    def analyze(self, twin_state):

        situation = {
            "status": "normal",
            "title": "Operations Stable",
            "explanation": [],
            "priority": "low"
        }

        risks = getattr(twin_state, "risks", [])

        if risks:

            situation["status"] = "attention_required"
            situation["priority"] = "high"
            situation["title"] = "Operational Risk Detected"

            for risk in risks:

                if risk["type"] == "cold_chain_breach":

                    situation["explanation"].append(
                        "Temperature controlled inventory may be damaged"
                    )

                elif risk["type"] == "capacity_shortage":

                    situation["explanation"].append(
                        "Capacity limitation may impact delivery SLA"
                    )

        return situation
