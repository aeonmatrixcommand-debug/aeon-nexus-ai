from datetime import datetime


class ApprovalGate:

    def __init__(self):
        self.records=[]


    def approve(self, action):

        record={
            "action":action,
            "approved":True,
            "timestamp":datetime.utcnow().isoformat()
        }

        self.records.append(record)

        return record


    def history(self):
        return self.records
