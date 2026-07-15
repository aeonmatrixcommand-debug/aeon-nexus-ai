
class AgentLearningEngine:

    def __init__(self):
        self.history = {}

    def record_result(
        self,
        agent_id,
        task_id,
        success,
        score
    ):

        if agent_id not in self.history:
            self.history[agent_id] = []

        self.history[agent_id].append(
            {
                "task_id": task_id,
                "success": success,
                "score": score
            }
        )


    def evaluate_performance(
        self,
        agent_id
    ):

        records = self.history.get(
            agent_id,
            []
        )

        if not records:
            return 0


        total = sum(
            item["score"]
            for item in records
        )

        return total / len(records)


    def generate_feedback(
        self,
        agent_id
    ):

        score = self.evaluate_performance(
            agent_id
        )

        if score >= 0.8:
            return "Excellent performance"

        if score >= 0.5:
            return "Needs improvement"

        return "Requires training"

