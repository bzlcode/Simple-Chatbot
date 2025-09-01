#AAH3 web_ui groq
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from ai_engine import get_groq_response

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("summarizer.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_groq_response(user_input)
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
