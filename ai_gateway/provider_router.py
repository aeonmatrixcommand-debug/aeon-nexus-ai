import os

from ai_gateway.gemini_provider import GeminiProvider
from ai_gateway.qwen_adapter import QwenAdapter


class ProviderRouter:

    def __init__(self):

        self.providers = {}

        # Gemini
        try:
            self.providers["gemini"] = GeminiProvider()
        except Exception:
            pass

        # Qwen
        try:
            self.providers["qwen"] = QwenAdapter(
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
        except Exception:
            pass

    def provider(self, name=None):

        if name is None:
            name = os.getenv(
                "AEON_LLM_PROVIDER",
                "gemini"
            )

        if name not in self.providers:
            raise ValueError(f"Unknown provider: {name}")

        return self.providers[name]
