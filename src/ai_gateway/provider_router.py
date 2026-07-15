class ProviderRouter:
    """
    Route requests to suitable AI model.
    """

    def route(self, task):

        task = task.lower()

        reasoning_keywords = [
            "analyze",
            "analysis",
            "reasoning",
            "decision",
            "risk",
            "strategy"
        ]

        forecast_keywords = [
            "forecast",
            "prediction",
            "demand",
            "trend"
        ]

        if any(
            word in task
            for word in reasoning_keywords
        ):
            return "gemini"


        if any(
            word in task
            for word in forecast_keywords
        ):
            return "gemini"


        return "default"
