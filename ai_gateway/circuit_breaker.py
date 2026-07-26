from datetime import datetime


class CircuitBreaker:

    def __init__(self, threshold=3):
        self.threshold = threshold
        self.failures = {}
        self.state = {}

    def record_success(self, provider):

        self.failures[provider] = 0
        self.state[provider] = {
            "status": "CLOSED",
            "updated": datetime.utcnow().isoformat()
        }


    def record_failure(self, provider):

        if provider not in self.failures:
            self.failures[provider] = 0

        self.failures[provider] += 1


        if self.failures[provider] >= self.threshold:
            self.state[provider] = {
                "status": "OPEN",
                "updated": datetime.utcnow().isoformat()
            }

        else:
            self.state[provider] = {
                "status": "DEGRADED",
                "updated": datetime.utcnow().isoformat()
            }


    def allow(self, provider):

        status = self.state.get(
            provider,
            {"status":"CLOSED"}
        )

        return status["status"] != "OPEN"


    def report(self):
        return self.state
