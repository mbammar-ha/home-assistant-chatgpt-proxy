import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read OpenAI key securely from environment variable
API_KEY = os.environ.get("OPENAI_API_KEY")  # Home Assistant injects it from secrets or add-on options

if not API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Add it in HA secrets or add-on options.")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": data["message"]}]
    }

    r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=body)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
