from causal_intelligence.causal_graph import CausalGraph
from causal_intelligence.root_cause_engine import RootCauseEngine
from causal_intelligence.prevention_engine import PreventionEngine



class CausalRuntime:


    def __init__(self):

        self.graph = CausalGraph()
        self.root = RootCauseEngine()
        self.prevent = PreventionEngine()



    def analyze(self,event):


        graph = self.graph.build(event)


        cause = self.root.analyze(
            graph
        )


        prevention = self.prevent.recommend(
            cause
        )


        return {

            "causal_graph":
            graph,

            "root_cause":
            cause,

            "prevention":
            prevention,

            "status":
            "causal_intelligence_ready"

        }
