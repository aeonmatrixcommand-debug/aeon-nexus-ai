import os

from google import genai
from google.genai.errors import ClientError


def generate(prompt: str) -> str:
    if os.getenv("RUN_LIVE_TESTS") != "1":
        return "AI Runtime Ready (Mock)"

    try:
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except ClientError as e:
        if "429" in str(e):
            return "Gemini quota exhausted - fallback runtime active"

        raise
