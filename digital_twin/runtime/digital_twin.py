from datetime import datetime


class DigitalTwin:

    def __init__(self):
        self.status = "INITIALIZED"
        self.entities = {}

    def sync(self, entity, data):

        self.entities[entity] = {
            "data": data,
            "updated_at": datetime.utcnow().isoformat()
        }

        self.status = "SYNCED"

        return {
            "twin_status": self.status,
            "entity": entity,
            "updated_at": self.entities[entity]["updated_at"]
        }


    def get_state(self):

        return {
            "status": self.status,
            "entities": self.entities
        }
