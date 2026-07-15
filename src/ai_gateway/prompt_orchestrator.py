class PromptOrchestrator:
    """
    Build AI instructions from enterprise context.
    """

    def build(
        self,
        task,
        context=None
    ):

        return {
            "system_role":
                "AEON MATRIX Enterprise Intelligence Agent",

            "task":
                task,

            "context":
                context or {},

            "execution_mode":
                "governed_autonomous"
        }
