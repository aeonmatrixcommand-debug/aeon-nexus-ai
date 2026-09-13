class ProviderRouter:

    def __init__(self):
        self.providers = []
        self.metrics = {}

    def register(self, name, provider):
        if name in self.metrics:
            raise ValueError("duplicate_provider")
        self.providers.append({
            "name": name,
            "provider": provider
        })

        self.metrics[name] = {
            "success": 0,
            "error": 0
        }


    def execute(self, prompt, breaker=None, *, provider_name=None, generate_only=False):
        """Invoke exactly one provider, with no fallback on failure.

        AEONAI's legacy execute(prompt, breaker) is supported when exactly one
        provider is registered. GovernedAnalysis selects its provider by name.
        Multiple registrations require a name; chat compatibility remains for
        legacy adapters, while the advisory boundary opts into generate_only.
        """

        errors = []

        selected = [item for item in self.providers
                    if provider_name is None or item["name"] == provider_name]
        if len(selected) != 1:
            return {"status": "FAILED", "errors": [{"error": "provider_selection_failed"}]}

        for item in selected:

            name = item["name"]
            provider = item["provider"]

            try:

                if breaker and not breaker.allow(name):
                    return {"status": "FAILED", "errors": [{"error": "circuit_open"}]}

                if generate_only:
                    result = provider.generate(prompt)
                elif hasattr(provider, "chat"):
                    result = provider.chat(prompt)

                else:
                    result = provider.generate(prompt)


                self.metrics[name]["success"] += 1

                if breaker:
                    breaker.record_success(name)
                return {
                    "provider": name,
                    "result": result
                }


            except Exception:

                self.metrics[name]["error"] += 1
                if breaker:
                    breaker.record_failure(name)
                errors.append(
                    {
                        "provider": name,
                        "error": "provider_failed"
                    }
                )


        return {
            "status": "FAILED",
            "errors": errors
        }


    def report(self):
        return self.metrics
