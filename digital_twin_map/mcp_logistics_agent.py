import json


class LogisticsAgent:


    def query(self,question):

        with open(
            "digital_twin_map/mock/logistics_world.json"
        ) as f:

            world=json.load(f)


        if "risk" in question.lower():

            return {

              "analysis":
              "DC-002 capacity approaching limit",

              "recommendation":
              "redistribute inventory"

            }


        if "route" in question.lower():

            return {

              "optimization":
              "TRUCK-042 reroute recommended",

              "saving":
              "18 minutes"

            }


        return world



if __name__=="__main__":

    ai=LogisticsAgent()

    print(
        json.dumps(
            ai.query(
            "find logistics risk"
            ),
            indent=2
        )
    )
