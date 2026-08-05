from qwen_agent.agents import Assistant


class QwenAdapter:
    """
    Qwen-Agent adapter for AEON-MATRIX.
    Exposes the same interface as GeminiProvider: generate(prompt) -> str
    """

    def __init__(self, llm_cfg: dict):
        self.agent = Assistant(
            llm=llm_cfg,
            system_message="You are AEON MATRIX Mother Brain AI."
        )

    def generate(self, prompt: str) -> str:
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        response = self.agent.run_nonstream(messages)

        if isinstance(response, list) and response:
            last = response[-1]

            if isinstance(last, dict):
                return str(last.get("content", ""))

            if hasattr(last, "content"):
                return str(last.content)

        return str(response)

    # Backward compatibility
    chat = generate
