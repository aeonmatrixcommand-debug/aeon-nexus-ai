from datetime import datetime


class Telemetry:

    def __init__(self):
        self.records = []


    def capture(
        self,
        provider,
        request,
        response
    ):

        record = {
            "provider": provider,
            "request": request,
            "response": response,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.records.append(record)

        return record


    def report(self):
        return self.records
