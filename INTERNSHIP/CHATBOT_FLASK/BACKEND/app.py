from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_text = data.get("text", "").strip().lower()

    if user_text == "":
        reply = "Please say something."
    
    elif "hello" in user_text:
        reply = "Hello! How can I assist you today?"

    elif "show me" in user_text:
        reply = f"Sure! Showing results for: {data.get('text')}"

    elif "calculate" in user_text and "stats" in user_text:
        month = data.get("text")
        reply = f"Calculating stats for {month}..."

    elif "clear chat" in user_text:
        reply = "Chat cleared!"

    else:
        reply = f"You said: {data.get('text')}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
