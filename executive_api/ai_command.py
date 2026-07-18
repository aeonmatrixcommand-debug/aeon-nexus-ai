from ai_gateway.copilot import AICopilot


class AICommand:

    def execute(self, event):

        return AICopilot().analyse(event)
