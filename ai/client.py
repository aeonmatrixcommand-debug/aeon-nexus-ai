<<<<<<< HEAD
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
=======
from google import genai
from ai.config import API_KEY

client = genai.Client(api_key=API_KEY)

def generate(prompt, model="gemini-3.5-flash"):
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text
>>>>>>> 60b4512 (chore: baseline verified before sprint 78 (169 tests passed))
