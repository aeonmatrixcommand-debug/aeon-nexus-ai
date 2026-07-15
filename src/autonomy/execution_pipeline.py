from autonomy.agent_runtime import AgentRuntime


class ExecutionPipeline:

    def __init__(self):

        self.agent_runtime = AgentRuntime()


    def execute(self, task):

        return self.agent_runtime.run(task)
