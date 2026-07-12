class DriverFeedbackLoop:

    def analyze(self, feedback):
        score = feedback.get("score", 0)

        return {
            "driver_status": "good" if score >= 80 else "review"
        }
