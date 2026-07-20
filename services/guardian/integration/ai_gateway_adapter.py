from services.guardian.contracts.runtime_signal import RuntimeSignal


class AIGatewayAdapter:

    def request(self, module, context):
        return RuntimeSignal(
            module=module,
            event_type="AI_DECISION",
            decision="OPTIMIZE_ALLOCATION",
            confidence=0.94,
            risk_score=0.10,
        )

    def validate(self, signal):
        return signal.confidence >= 0.80
