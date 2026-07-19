import json
from datetime import datetime, UTC


class MCPToolRouter:


    def execute(self, intent):

        tools = {

            "fleet":
            "Fleet Digital Twin",

            "warehouse":
            "Warehouse Twin",

            "inventory":
            "Inventory Intelligence",

            "risk":
            "Risk Prediction Engine"

        }


        return {

            "intent": intent,

            "tool_selected":

            tools.get(
                intent,
                "General Intelligence"
            )

        }



class GeminiProEnterpriseAgent:


    def reason(self, command):

        command = command.lower()


        if "fleet" in command:

            intent="fleet"

        elif "warehouse" in command:

            intent="warehouse"

        elif "inventory" in command:

            intent="inventory"

        else:

            intent="risk"



        action = MCPToolRouter().execute(
            intent
        )


        return {

            "model":

            "Gemini Pro Latest",


            "command":

            command,


            "reasoning":

            action,


            "recommendation":

            "ANALYSIS_READY"

        }



if __name__=="__main__":


    result = GeminiProEnterpriseAgent().reason(

        "Analyze fleet delay risk"

    )


    print(
        json.dumps(
            result,
            indent=2
        )
    )

