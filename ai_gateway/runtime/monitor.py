
class RuntimeMonitor:


    def __init__(self):
        self.metrics=[]


    def observe(self, execution):

        result={
            "execution": execution,
            "health": "NORMAL"
        }

        self.metrics.append(result)

        return result


    def report(self):
        return self.metrics
