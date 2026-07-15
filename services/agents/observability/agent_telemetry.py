
class AgentTelemetryCollector:

    def __init__(self):
        self.events = []


    def record_execution(
        self,
        agent_id,
        task_id,
        success
    ):

        self.events.append(
            {
                "type": "execution",
                "agent_id": agent_id,
                "task_id": task_id,
                "success": success
            }
        )


    def record_latency(
        self,
        agent_id,
        latency_ms
    ):

        self.events.append(
            {
                "type": "latency",
                "agent_id": agent_id,
                "latency_ms": latency_ms
            }
        )


    def record_error(
        self,
        agent_id,
        error
    ):

        self.events.append(
            {
                "type": "error",
                "agent_id": agent_id,
                "error": error
            }
        )


    def get_agent_metrics(
        self,
        agent_id
    ):

        records = [
            event
            for event in self.events
            if event["agent_id"] == agent_id
        ]

        executions = [
            e for e in records
            if e["type"] == "execution"
        ]

        success_count = len(
            [
                e for e in executions
                if e["success"]
            ]
        )

        return {
            "total_events": len(records),
            "executions": len(executions),
            "success_rate":
                (
                    success_count /
                    len(executions)
                )
                if executions else 0
        }

