from datetime import datetime


class DecisionFeedback:


    def __init__(self):
        self.records=[]


    def capture(self,action,result):

        record={
            "action":action,
            "result":result,
            "timestamp":datetime.utcnow().isoformat()
        }

        self.records.append(record)

        return record


    def history(self):
        return self.records
