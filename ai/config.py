import os

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
API_KEY = os.getenv("GEMINI_API_KEY")
TIMEOUT = int(os.getenv("GEMINI_TIMEOUT", "30"))
