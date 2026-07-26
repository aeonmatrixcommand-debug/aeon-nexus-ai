from qwen_agent.agents import Assistant


class QwenAdapter:
    """
    Qwen-Agent adapter for AEON MATRIX Gateway
    """

    def __init__(self, llm_cfg: dict):
        self.agent = Assistant(
            llm=llm_cfg
        )

    def chat(self, prompt: str):

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        result = self.agent.run_nonstream(messages)

        if isinstance(result, list):
            return result[-1].get(
                "content",
                str(result)
            )

        return str(result)
