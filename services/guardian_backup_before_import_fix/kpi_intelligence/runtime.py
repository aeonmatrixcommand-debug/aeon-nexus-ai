class KPIIntelligenceEngine:

    def evaluate(self, metrics):
        otif = metrics.get("otif", 0)
        sla = metrics.get("sla", 0)

        return {
            "otif_status": "healthy" if otif >= 95 else "risk",
            "sla_status": "healthy" if sla >= 95 else "risk"
        }
