class HealthCheck:
    @staticmethod
    def report(registry):
        print("\n========== SYSTEM HEALTH ==========")
        for name, status in registry.list_services().items():
            print(f"[{status}] {name}")
        print("===================================")
