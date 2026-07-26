from ai_gateway.runtime.state import AgentState
from ai_gateway.runtime.registry import AgentRegistry
from ai_gateway.runtime.scheduler import AgentScheduler
from ai_gateway.runtime.executor import RuntimeExecutor


class AgentRuntime:


    def __init__(self):

        self.state = AgentState()
        self.registry = AgentRegistry()
        self.scheduler = AgentScheduler()
        self.executor = RuntimeExecutor()


    def start(self):

        self.state.update("READY")


    def run(self, task):

        self.state.update("EXECUTING")

        scheduled = self.scheduler.schedule(task)

        result = self.executor.execute(
            scheduled
        )

        self.state.update("COMPLETED")

        return result
