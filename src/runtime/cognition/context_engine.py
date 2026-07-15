class ContextEngine:
    """
    Build operational context from current signals.
    """

    def build(self, event):

        return {
            "event": event,
            "context_type": "operational",
            "ready_for_reasoning": True
        }
