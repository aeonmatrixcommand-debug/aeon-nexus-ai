from datetime import datetime


class AuditTrail:

    def __init__(self):
        self.logs=[]


    def record(self,event):

        self.logs.append({
            "event":event,
            "time":datetime.utcnow().isoformat()
        })


    def report(self):
        return self.logs
