import os
from google import genai


class GeminiProvider:

    def __init__(self):

        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY missing"
            )

        self.client = genai.Client(
            api_key=api_key
        )


    def generate(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        return response.text
