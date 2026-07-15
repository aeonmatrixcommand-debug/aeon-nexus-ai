from ai_gateway.model_registry import ModelRegistry
from ai_gateway.provider_router import ProviderRouter
from ai_gateway.context_manager import ContextManager
from ai_gateway.prompt_orchestrator import PromptOrchestrator


class AIGateway:

    def __init__(self):

        self.models = ModelRegistry()
        self.router = ProviderRouter()
        self.context = ContextManager()
        self.prompt = PromptOrchestrator()


    def initialize(self):

        self.models.register(
            "gemini",
            "google",
            [
                "reasoning",
                "forecast",
                "analysis"
            ]
        )


    def process(self, task):

        model = self.router.route(task)

        prompt = self.prompt.build(
            task,
            self.context.get_context()
        )

        return {
            "model": model,
            "prompt": prompt,
            "status": "ready_for_execution"
        }


if __name__ == "__main__":

    gateway = AIGateway()

    gateway.initialize()

    print(
        gateway.process(
            "analyze warehouse risk"
        )
    )
