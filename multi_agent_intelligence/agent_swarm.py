import json
from datetime import datetime



class AgentRegistry:


    def load_agents(self):

        return [

            {
                "name":
                "Guardian AI",

                "role":
                "Risk Governance"
            },

            {
                "name":
                "Forecast AI",

                "role":
                "Demand Prediction"
            },

            {
                "name":
                "Recovery AI",

                "role":
                "Autonomous Recovery"
            },

            {
                "name":
                "Optimization AI",

                "role":
                "Resource Optimization"
            }

        ]



class AgentCommunicationBus:


    def broadcast(self,task,agents):

        messages=[]


        for agent in agents:

            messages.append({

                "agent":
                    agent["name"],

                "task":
                    task,

                "status":
                    "ANALYZING"

            })


        return messages




class TaskAllocator:


    def assign(self,messages):

        return [

            {

            "agent":
                msg["agent"],

            "decision":
                "PROCESS_TASK"

            }

            for msg in messages

        ]




class ConsensusEngine:


    def evaluate(self,decisions):

        return {

            "consensus":
                "APPROVED",

            "agreement_score":
                96,

            "action":
                "EXECUTE_OPTIMIZED_PLAN"

        }




class AgentSwarm:


    def run(self,task):

        agents = AgentRegistry().load_agents()


        communication = (
            AgentCommunicationBus()
            .broadcast(task,agents)
        )


        decisions = (
            TaskAllocator()
            .assign(communication)
        )


        consensus = (
            ConsensusEngine()
            .evaluate(decisions)
        )


        return {

            "system":
            "AEON MATRIX MULTI AGENT INTELLIGENCE",


            "timestamp":
            datetime.utcnow().isoformat(),


            "agents":
            agents,


            "communication":
            communication,


            "decisions":
            decisions,


            "consensus":
            consensus

        }




if __name__=="__main__":


    print("="*75)

    print(
        " AEON MATRIX AGENT SWARM INTELLIGENCE "
    )

    print("="*75)


    task = (
        "Optimize warehouse operations "
        "under high demand"
    )


    print(
        json.dumps(
            AgentSwarm().run(task),
            indent=2
        )
    )

