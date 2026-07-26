from datetime import datetime


class Executor:


    def __init__(self):
        self.logs = []


    def execute(self, action):

        result = {
            "action": action,
            "status": "SIMULATED",
            "timestamp": datetime.utcnow().isoformat()
        }


        self.logs.append(result)

        return result


    def report(self):
        return self.logs
