class AgentBus:


    def send(self,agent,message):


        return {

            "agent":agent,

            "message":message,

            "status":"received"

        }
