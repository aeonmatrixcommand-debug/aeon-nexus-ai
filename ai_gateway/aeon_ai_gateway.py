import os

from ai_gateway.gemini_provider import GeminiProvider
from ai_gateway.qwen_adapter import QwenAdapter
from ai_gateway.health import ProviderHealth
from ai_gateway.router import ProviderRouter
from ai_gateway.metrics import GatewayMetrics


class AEONAI:

    def __init__(self, provider=None):
        self.health = ProviderHealth()
        self.router = ProviderRouter()
        self.metrics = GatewayMetrics()

        provider = provider or os.getenv(
            "AEON_LLM_PROVIDER",
            "gemini"
        )

        if provider == "qwen":

            self.provider = QwenAdapter(
                {
                    "model": os.getenv(
                        "QWEN_MODEL",
                        "qwen-max"
                    ),
                    "api_key": os.getenv(
                        "DASHSCOPE_API_KEY",
                        ""
                    )
                }
            )

            self.mode = "qwen"

        else:

            self.provider = GeminiProvider()
            self.mode = "gemini"

        self.health.check(self.mode, self.provider)
        self.router.register(self.mode, self.provider)


    def analyze(self, event):

        prompt = f"""
You are AEON MATRIX Mother Brain AI.

Analyze operational event:

{event}

Return:

1. Situation
2. Risk
3. Prediction
4. Recommended Action
"""


        return self.router.execute(prompt)


        return self.router.execute(prompt)
