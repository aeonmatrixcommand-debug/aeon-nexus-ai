from datetime import datetime


class DigitalTwinFeedback:

    def update(self, execution):

        return {
            "twin_status": "SYNCED",
            "execution_status": execution["status"],
            "updated_at": datetime.utcnow().isoformat()
        }
