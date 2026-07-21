class ExecutiveAPI:
    def health(self):
        return {"status": "healthy"}

    def kpi(self):
        return {
            "otif": 98,
            "sla": 99,
            "inventory_accuracy": 99.8
        }
