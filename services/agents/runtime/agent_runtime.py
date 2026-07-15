from .agent_result import AgentResult


class AgentRuntime:

    def __init__(
        self,
        registry,
        router,
        policy,
        memory
    ):
        self.registry = registry
        self.router = router
        self.policy = policy
        self.memory = memory


    def execute(self, task):

        agent = self.router.route(task.capability)

        if agent is None:
            return AgentResult(
                success=False,
                agent_name="none",
                output={},
                message="No agent found"
            )

        if not self.policy.validate(agent):
            return AgentResult(
                success=False,
                agent_name=agent.name,
                output={},
                message="Governance blocked"
            )

        self.memory.remember(
            task.task_id,
            task.payload
        )

        return AgentResult(
            success=True,
            agent_name=agent.name,
            output={
                "status": "executed",
                "capability": task.capability
            }
        )
