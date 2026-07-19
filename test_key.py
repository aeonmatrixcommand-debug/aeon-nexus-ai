import os
from google import genai

key = os.environ.get("GEMINI_API_KEY")

print("KEY PREFIX:", key[:10] if key else "NONE")

client = genai.Client(
    api_key=key
)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Reply AEON MATRIX ONLINE"
)

print(response.text)
