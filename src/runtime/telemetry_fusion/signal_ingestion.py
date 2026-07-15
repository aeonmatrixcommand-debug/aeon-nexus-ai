class SignalIngestion:
    """
    Collect external and operational signals.
    """

    def ingest(self, signal):

        return {
            "signal": signal,
            "status": "received",
            "source": signal.get("source", "unknown")
        }
