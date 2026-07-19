from datetime import datetime


class ValueRecoveryEngine:

    def analyze(self, shelf_life_days):

        if shelf_life_days <= 3:
            action = "PROMOTION_OR_PROCESSING"

        else:
            action = "NORMAL_FLOW"

        return {
            "shelf_life_days": shelf_life_days,
            "recommendation": action,
            "generated_at": datetime.utcnow().isoformat()
        }
