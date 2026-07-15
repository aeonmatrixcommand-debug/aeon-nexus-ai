class SensorFusion:
    """
    Combine multiple operational signals.
    """

    def combine(self, signals):

        risk = "normal"

        for signal in signals:

            if signal.get("temperature") == "warning":
                risk = "cold_chain_risk"

        return {
            "combined_signals": signals,
            "risk_state": risk,
            "fusion_status": "completed"
        }
