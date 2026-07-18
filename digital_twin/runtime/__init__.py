from datetime import datetime


class DigitalTwin:

    def __init__(self):
        self.state = {}

    def sync(self, entity, data=None):

        if data is None:
            data = {
                "status": "SYNCED",
                "source": "ENTERPRISE_CONTROL_CENTER"
            }

        self.state[entity] = {
            "data": data,
            "updated_at": datetime.utcnow().isoformat()
        }

        return {
            "twin_status": "SYNCED",
            "entity": entity,
            "data": data,
            "updated_at": self.state[entity]["updated_at"]
        }

    def get_state(self):
        return self.state
