class ShelfLifeIntelligence:

    def analyze(self, days_remaining):

        if days_remaining <= 3:
            status = "CRITICAL"
            action = "FAST_TRACK_PROCESSING"

        elif days_remaining <= 7:
            status = "WARNING"
            action = "PROMOTION_OR_REBALANCE"

        else:
            status = "HEALTHY"
            action = "NORMAL_FLOW"

        return {
            "shelf_life_status": status,
            "recommended_action": action
        }
