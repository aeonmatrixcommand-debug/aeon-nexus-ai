class DecisionRuntimeBridge:

    def publish(self, decision):

        return {
            "runtime_event": "DECISION_CREATED",
            "decision": decision["decision"],
            "action": decision["action"],
            "confidence": decision["confidence"]
        }
