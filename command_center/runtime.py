class CommandCenter:

    def monitor(self, data):

        return {
            "command_center": "ONLINE",
            "alerts": data,
            "status": "MONITORING"
        }
