import os
from google import genai
from google.genai.errors import ClientError


def generate(prompt: str) -> str:

    if os.getenv("RUN_LIVE_TESTS") != "1":
        return "AI Runtime Mock Ready"

    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(
        api_key=api_key
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except ClientError as e:

        if e.code == 429:
            return "AI Runtime Quota Limited - Fallback Mode"

        raise
