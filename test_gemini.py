import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="ตอบกลับเพียงคำว่า เชื่อมต่อสำเร็จ"
)

print(response.text)
