class ActionRegistry:
    """
    AEON MATRIX Action Registry.
    Central catalog for autonomous actions.
    """

    def __init__(self):
        self.actions = {
            "move_to_backup_storage": {
                "type": "warehouse_action",
                "risk": "high"
            },
            "optimize_capacity": {
                "type": "optimization_action",
                "risk": "medium"
            }
        }


    def get(self, action):

        return self.actions.get(
            action,
            {
                "type": "unknown",
                "risk": "unknown"
            }
        )
