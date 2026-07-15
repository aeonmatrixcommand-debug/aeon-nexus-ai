class EventStore:


    def __init__(self):

        self.events=[]



    def record(self,event):

        self.events.append(event)


        return {
            "stored":True,
            "event":event
        }



    def history(self):

        return self.events
