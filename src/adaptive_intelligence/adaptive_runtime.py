from adaptive_intelligence.confidence_calibrator import ConfidenceCalibrator
from adaptive_intelligence.behavior_optimizer import BehaviorOptimizer



class AdaptiveRuntime:


    def __init__(self):

        self.calibrator = ConfidenceCalibrator()
        self.optimizer = BehaviorOptimizer()



    def learn(self, decision, outcome, history):


        confidence = self.calibrator.calibrate(
            decision,
            outcome
        )


        behavior = self.optimizer.optimize(
            history
        )


        return {

            "decision":
            decision,


            "confidence_update":
            confidence,


            "behavior_learning":
            behavior,


            "status":
            "adaptive_learning_completed"

        }
