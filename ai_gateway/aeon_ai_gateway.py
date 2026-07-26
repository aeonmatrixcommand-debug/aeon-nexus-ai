import os

from ai_gateway.gemini_provider import GeminiProvider
from ai_gateway.qwen_adapter import QwenAdapter
from ai_gateway.health import ProviderHealth
from ai_gateway.router import ProviderRouter
from ai_gateway.metrics import GatewayMetrics
from ai_gateway.circuit_breaker import CircuitBreaker
from ai_gateway.events import EventBus
from ai_gateway.telemetry import Telemetry
from ai_gateway.risk import RiskAnalyzer
from ai_gateway.guardian import Guardian
from ai_gateway.decision import DecisionContract


class AEONAI:

    def __init__(self, provider=None):
        self.health = ProviderHealth()
        self.router = ProviderRouter()
        self.metrics = GatewayMetrics()
        self.breaker = CircuitBreaker()
        self.events = EventBus()
        self.telemetry = Telemetry()
        self.risk = RiskAnalyzer()
        self.guardian = Guardian()
        self.decision = DecisionContract()

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


        result = self.router.execute(
            prompt,
            self.breaker
        )


        self.events.publish(
            "AI_DECISION",
            {
                "provider": self.mode,
                "event": event
            }
        )


        self.telemetry.capture(
            self.mode,
            event,
            result
        )


        risk = self.risk.analyze(
            event
        )


        guardian_result = self.guardian.evaluate(
            risk
        )


        final_decision = self.decision.build(
            result,
            guardian_result
        )


        self.events.publish(
            "GUARDIAN_DECISION",
            final_decision
        )


        return final_decision

