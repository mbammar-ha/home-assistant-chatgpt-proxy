from flask import Flask, request, jsonify
import os, requests

app = Flask(__name__)
API_KEY = os.getenv("OPENAI_API_KEY", "")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": user_message}]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=body)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
