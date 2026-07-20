class OutcomeCollector:

    def collect(self, workflow):

        return {
            "execution_id": workflow["execution_id"],
            "success": workflow["state"] == "COMPLETED",
            "learning_signal": "POSITIVE"
        }
