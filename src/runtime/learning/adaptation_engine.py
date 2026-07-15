class AdaptationEngine:
    """
    Convert learning signals into future adaptation.
    """

    def adapt(self, behavior):

        return {
            "adapted": True,
            "next_behavior": behavior["strategy"],
            "learning_state": behavior["learning"]
        }
