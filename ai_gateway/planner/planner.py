from ai_gateway.planner.task import Task


class AgentPlanner:


    def __init__(self):
        self.plans = []


    def create_plan(self, goal):

        tasks = []

        objective = goal.objective.lower()


        if "isolation" in objective:

            tasks.append(
                Task(
                    "Analyze Threat",
                    "THREAT_ANALYSIS"
                )
            )

            tasks.append(
                Task(
                    "Execute Isolation",
                    "SYSTEM_ISOLATION"
                )
            )


        else:

            tasks.append(
                Task(
                    "General Execution",
                    "DEFAULT_ACTION"
                )
            )


        plan = {
            "goal": goal.to_dict(),
            "tasks": [
                task.to_dict()
                for task in tasks
            ]
        }


        self.plans.append(plan)

        return plan


    def history(self):
        return self.plans
