class DecisionMemory:


    def __init__(self):

        self.records=[]



    def remember(self,decision,result):

        self.records.append(
            {
                "decision":decision,
                "result":result
            }
        )



    def search(self,decision):

        return [

            item for item in self.records

            if item["decision"]==decision

        ]
