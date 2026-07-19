from datetime import datetime
import json


class DigitalTwin:

    def __init__(self):
        self.assets = {
            "warehouse": "ACTIVE",
            "inventory": "SYNCED",
            "fleet": "CONNECTED",
            "orders": "FLOWING"
        }


    def simulate(self, scenario):

        if scenario == "inventory_disruption":
            result = {
                "impact": "HIGH",
                "ot_if_risk": "INCREASED",
                "recommended_action":
                    "Inventory Re-Sync + Demand Rebalance"
            }

        elif scenario == "eta_failure":
            result = {
                "impact": "MEDIUM",
                "sla_risk": "DETECTED",
                "recommended_action":
                    "Route Optimization"
            }

        else:
            result = {
                "impact": "LOW",
                "recommended_action":
                    "Continue Normal Operation"
            }

        return result



class BusinessImpactSimulator:

    def evaluate(self, simulation):

        return {

            "financial_risk":
                "$42,000 potential exposure",

            "customer_impact":
                "SLA protection required",

            "operational_score":
                "92/100",

            "decision":
                simulation["recommended_action"]

        }



if __name__ == "__main__":

    twin = DigitalTwin()

    scenario = "inventory_disruption"

    simulation = twin.simulate(scenario)

    impact = BusinessImpactSimulator().evaluate(
        simulation
    )


    output = {

        "system":
        "AEON MATRIX DIGITAL TWIN ENGINE",

        "status":
        "ONLINE",

        "scenario":
        scenario,

        "simulation":
        simulation,

        "business_impact":
        impact,

        "timestamp":
        datetime.now().isoformat()

    }


    print("=================================")
    print(" AEON MATRIX DIGITAL TWIN ")
    print("=================================")

    print(
        json.dumps(
            output,
            indent=2
        )
    )

    print("=================================")
    print(" PREDICTIVE SCENARIO ENGINE ONLINE ")
    print(" Simulate > Predict > Optimize ")
    print("=================================")
