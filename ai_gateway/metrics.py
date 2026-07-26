from datetime import datetime


class GatewayMetrics:

    def __init__(self):
        self.data = {}

    def record(self, provider, success=True):

        if provider not in self.data:
            self.data[provider] = {
                "requests":0,
                "success":0,
                "errors":0,
                "updated":None
            }

        self.data[provider]["requests"] += 1

        if success:
            self.data[provider]["success"] += 1
        else:
            self.data[provider]["errors"] += 1

        self.data[provider]["updated"] = (
            datetime.utcnow().isoformat()
        )

        return self.data[provider]


    def report(self):
        return self.data
