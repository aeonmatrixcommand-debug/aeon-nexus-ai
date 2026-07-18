<<<<<<< HEAD
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
=======
import os

>>>>>>> 072e626 (fix: add Gemini quota fallback and runtime resilience)
from google import genai
from google.genai.errors import ClientError


<<<<<<< HEAD
def generate(prompt, model="gemini-3.5-flash"):
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text
>>>>>>> 60b4512 (chore: baseline verified before sprint 78 (169 tests passed))
=======
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
>>>>>>> 072e626 (fix: add Gemini quota fallback and runtime resilience)
