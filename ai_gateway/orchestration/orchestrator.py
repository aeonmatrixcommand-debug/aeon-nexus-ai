from ai_gateway.decision import DecisionEngine
from ai_gateway.memory import MemoryStore, ExperienceMemory
from ai_gateway.learning import FeedbackLoop


class AutonomousOrchestrator:

    def __init__(self):

        self.decision = DecisionEngine()

        self.memory_store = MemoryStore()

        self.memory = ExperienceMemory(
            self.memory_store
        )

        self.feedback = FeedbackLoop()


    def execute(self, action):

        decision = self.decision.analyze(
            action
        )

        result = {
            "action": action,
            "decision": decision,
            "status": "SIMULATED"
        }


        self.memory.learn(
            action,
            result
        )


        self.feedback.capture(
            action,
            result
        )


        return result


    def history(self):

        return {
            "memory":
                self.memory_store.recall(),

            "feedback":
                self.feedback.history(),

            "decision":
                self.decision.trace.history()
        }
