import os

from ai_gateway.gemini_provider import GeminiProvider
from ai_gateway.qwen_adapter import QwenAdapter
from ai_gateway.health import ProviderHealth


class AEONAI:

    def __init__(self, provider=None):
        self.health = ProviderHealth()

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


        if self.mode == "qwen":
            return self.provider.chat(prompt)


        return self.provider.generate(prompt)
