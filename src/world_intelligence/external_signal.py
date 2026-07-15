class ExternalSignalCollector:
    """
    Collect external world signals.
    """

    def collect(self, signal):

        return {
            "source": signal.get("source"),
            "category": signal.get("category"),
            "value": signal.get("value"),
            "status": "captured"
        }
