from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)

@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    prompt = data.get(
        "prompt",
        "AEON MATRIX ONLINE"
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return jsonify({
        "status": "SUCCESS",
        "response": response.text
    })


@app.route("/")
def health():

    return {
        "system": "AEON MATRIX GEMINI GATEWAY",
        "status": "ONLINE"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
