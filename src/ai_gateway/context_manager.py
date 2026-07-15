class ContextManager:
    """
    Manage enterprise AI context.
    """

    def __init__(self):
        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value

    def get_context(self):
        return self.context

    def clear(self):
        self.context = {}
