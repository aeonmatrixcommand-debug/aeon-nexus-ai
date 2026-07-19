from services.guardian.contracts.ai_runtime_event import AIRuntimeEvent


class AIGatewayAdapter:


    def request(
        self,
        module,
        input_data
    ):


        decision = "Increase Allocation"


        event = AIRuntimeEvent(
            source="AI_GATEWAY",
            module=module,
            event_type="AI_DECISION",
            decision=decision,
            confidence=0.94
        )


        return {
            "decision":decision,
            "confidence":0.94,
            "policy":"APPROVED",
            "trace_id":event.trace_id
        }
