class ImpactExplainer:
    """
    Explain business impact.
    """

    def explain(self, decision):

        if decision == "move_to_backup_storage":

            return {
                "risk_reduction": "85%",
                "sla_protection": "high",
                "business_impact":
                    "prevent_product_quality_loss"
            }


        return {
            "risk_reduction": "unknown",
            "sla_protection": "unknown",
            "business_impact":
                "not_available"
        }
