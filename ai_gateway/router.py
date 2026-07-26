class ProviderRouter:

    def __init__(self):
        self.providers = []
        self.metrics = {}

    def register(self, name, provider):
        self.providers.append({
            "name": name,
            "provider": provider
        })

        self.metrics[name] = {
            "success": 0,
            "error": 0
        }


    def execute(self, prompt, breaker=None):

        errors = []

        for item in self.providers:

            name = item["name"]
            provider = item["provider"]

            try:

                if hasattr(provider, "chat"):
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


            except Exception as e:

                self.metrics[name]["error"] += 1
                errors.append(
                    {
                        "provider": name,
                        "error": str(e)
                    }
                )


        return {
            "status": "FAILED",
            "errors": errors
        }


    def report(self):
        return self.metrics
