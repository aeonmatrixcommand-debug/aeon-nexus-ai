from datetime import datetime


class ProviderHealth:
    """
    AI Provider health monitoring.
    """

    def __init__(self):
        self.status = {}

    def check(self, name, provider):
        result = {
            "provider": name,
            "status": "UNKNOWN",
            "timestamp": datetime.utcnow().isoformat()
        }

        try:
            if provider:
                result["status"] = "AVAILABLE"
            else:
                result["status"] = "UNAVAILABLE"

        except Exception as e:
            result["status"] = "ERROR"
            result["error"] = str(e)

        self.status[name] = result
        return result

    def report(self):
        return self.status
