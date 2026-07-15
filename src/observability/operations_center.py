from observability.metrics_collector import MetricsCollector
from observability.agent_trace import AgentTrace
from observability.decision_timeline import DecisionTimeline
from observability.health_monitor import HealthMonitor



class OperationsCenter:


    def __init__(self):

        self.metrics = MetricsCollector()

        self.trace = AgentTrace()

        self.timeline = DecisionTimeline()

        self.health = HealthMonitor()



    def monitor(self, event):


        self.timeline.add(
            "event_received",
            event
        )


        self.metrics.record(
            "decision_latency",
            "120ms"
        )


        self.trace.capture(
            "risk_agent",
            "analyze_temperature_warning"
        )


        return {


            "health":
            self.health.check(),


            "metrics":
            self.metrics.snapshot(),


            "trace":
            self.trace.history(),


            "timeline":
            self.timeline.events

        }
