class SignalCollector:
    """
    Collect external world signals.
    """

    def collect(self, signals):

        return {
            "signals": signals,
            "signal_count": len(signals)
        }
