from datetime import datetime


class FeedbackLoop:

    def __init__(self):
        self.records = []


    def capture(self, action, result):

        self.records.append({
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "result": result
        })


    def history(self):

        return self.records
