from services.guardian.contracts.runtime_signal import RuntimeSignal


class RuntimeTelemetryPublisher:

    def publish(self, signal: RuntimeSignal):
        return {
            "topic": "guardian.decision",
            "module": signal.module,
            "decision": signal.decision,
            "confidence": signal.confidence,
            "trace_id": signal.trace_id,
            "timestamp": signal.timestamp,
        }
