class RealTimeCommandCenter:

    def monitor(self, event):
        severity = event.get("severity", "normal")

        return {
            "status": "alert" if severity == "critical" else "monitoring",
            "source": event.get("source", "unknown")
        }
