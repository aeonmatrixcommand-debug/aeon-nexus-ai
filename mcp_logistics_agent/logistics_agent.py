import json
from datetime import datetime, UTC



class LogisticsKnowledge:


    def get_context(self):

        return {

            "fleet":

            {

            "active_vehicle":420,

            "late_risk":12

            },


            "warehouse":

            {

            "capacity":82,

            "picking_delay":7

            },


            "inventory":

            {

            "health":91,

            "expiry_risk":8

            },


            "otif":

            96

        }




class MCPLogisticsAgent:


    def analyze(self,command):


        data = LogisticsKnowledge().get_context()


        command = command.lower()


        if "otif" in command:

            return {


            "question":command,


            "analysis":

            "OTIF performance impacted by fleet delay",


            "root_cause":

            [

            "Traffic congestion",

            "Warehouse picking pressure"

            ],


            "recommendation":

            "Activate route optimization"

            }



        if "truck" in command or "vehicle" in command:

            return {


            "high_risk_assets":

            [

            {

            "id":"TRUCK-042",

            "risk":"HIGH",

            "eta_delay":"+32 min"

            }

            ],


            "action":

            "REROUTE"

            }



        return {


            "message":

            "Command understood",


            "available":

            [

            "fleet analysis",

            "otif investigation",

            "inventory risk",

            "simulation"

            ]

        }




class ExecutiveAssistant:


    def respond(self,result):

        return {


        "timestamp":

        datetime.now(UTC).isoformat(),


        "agent":

        "AEON MATRIX LOGISTICS COMMAND AI",


        "response":

        result

        }




if __name__=="__main__":


    command = "Why OTIF dropped today"


    result = MCPLogisticsAgent().analyze(
        command
    )


    print("="*70)

    print(
    " AEON MATRIX MCP LOGISTICS COMMAND AGENT "
    )

    print("="*70)


    print(

    json.dumps(

    ExecutiveAssistant().respond(result),

    indent=2

    )

    )

