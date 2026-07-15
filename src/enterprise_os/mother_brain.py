class MotherBrain:


    def __init__(self):

        self.systems=[]



    def register(self,name):

        self.systems.append(name)



    def status(self):

        return {

            "registered_systems":
            self.systems,

            "brain_status":
            "operational"

        }
