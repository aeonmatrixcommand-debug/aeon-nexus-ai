class DiscoveryEngine:


    def discover(self,task):


        mapping={

            "risk":
            "risk_agent",

            "forecast":
            "forecast_agent",

            "finance":
            "finance_agent",

            "maintenance":
            "maintenance_agent"

        }


        selected=[]


        for key,value in mapping.items():

            if key in task:

                selected.append(value)


        return {

            "task":task,

            "recommended_agents":selected,

            "status":"discovered"

        }
