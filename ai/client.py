from google import genai
from ai.config import API_KEY

client = genai.Client(api_key=API_KEY)

def generate(prompt, model="gemini-3.5-flash"):
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text
