class AgentKPI:

    def __init__(self):
        self.metrics = {}

    def record_execution(
        self,
        agent_name,
        success=True,
        latency_ms=0,
        business_value=0
    ):
        if agent_name not in self.metrics:
            self.metrics[agent_name] = {
                "executions": 0,
                "success": 0,
                "errors": 0,
                "latency_total": 0,
                "business_value": 0
            }

        metric = self.metrics[agent_name]

        metric["executions"] += 1
        metric["latency_total"] += latency_ms
        metric["business_value"] += business_value

        if success:
            metric["success"] += 1
        else:
            metric["errors"] += 1


    def get_score(self, agent_name):

        metric = self.metrics.get(agent_name)

        if not metric:
            return None

        executions = metric["executions"]

        success_rate = (
            metric["success"] / executions
            if executions else 0
        )

        avg_latency = (
            metric["latency_total"] / executions
            if executions else 0
        )

        return {
            "agent_name": agent_name,
            "execution_count": executions,
            "success_rate": success_rate,
            "average_latency_ms": avg_latency,
            "business_value": metric["business_value"]
        }
