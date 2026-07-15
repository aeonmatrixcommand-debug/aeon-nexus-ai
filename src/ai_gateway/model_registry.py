class ModelRegistry:
    """
    Registry for AI model providers.
    """

    def __init__(self):
        self.models = {}

    def register(
        self,
        name,
        provider,
        capability
    ):
        self.models[name] = {
            "provider": provider,
            "capability": capability
        }

    def get(self, name):
        return self.models.get(name)

    def list_models(self):
        return self.models
