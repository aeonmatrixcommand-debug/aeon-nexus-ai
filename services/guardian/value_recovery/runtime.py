class ValueRecoveryIntelligence:

    def recover(self, item):
        value = item.get("recoverable_value", 0)

        return {
            "recovered_value": value,
            "action": "recover" if value > 0 else "discard"
        }
