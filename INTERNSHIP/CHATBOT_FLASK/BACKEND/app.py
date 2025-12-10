from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/chat")
def chat():
    data = request.get_json()
    user_text = data.get("text", "")
    
    reply = f"You said: {user_text}"

    return jsonify({"reply": reply})

app.run(debug=True)
