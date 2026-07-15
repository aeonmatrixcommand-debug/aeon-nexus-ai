class SharedContext:
    """
    Common understanding between human and AI.
    """

    def build(self, situation, reason):

        return {
            "situation": situation,
            "reason": reason,
            "alignment": "shared"
        }
