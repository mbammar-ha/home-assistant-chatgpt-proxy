import os, requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read from environment variable (if set) or fallback to options
API_KEY = os.getenv("OPENAI_API_KEY", "sk-xxxxxx-your-key")  # replace with your key

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
    r = requests.post("https://api.openai.com/v1/chat/completions", json=body, headers=headers)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
