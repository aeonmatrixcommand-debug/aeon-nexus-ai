class ResultAggregator:

    def __init__(self):
        self.results = {}

    def add_result(
        self,
        agent_name,
        result
    ):
        self.results[agent_name] = result


    def combine(self):

        return self.results
