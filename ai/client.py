import os

from google import genai
from google.genai.errors import ClientError


def generate(prompt: str, model: str = "gemini-3.5-flash") -> str:
    """Generate content using Gemini with mock mode and quota fallback."""

    if os.getenv("RUN_LIVE_TESTS") != "1":
        return "AI Runtime Mock Ready"

    api_key = os.getenv("GEMINI_API_KEY")
<<<<<<< HEAD

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

=======
>>>>>>> origin/main
    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        return response.text

    except ClientError as e:
        if getattr(e, "code", None) == 429:
            return "AI Runtime Quota Limited - Fallback Mode"
        raise
