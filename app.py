import os
import json
import random
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load intents
try:
    with open('intents.json', 'r') as file:
        intents_data = json.load(file)
        intents = intents_data['intents']
except FileNotFoundError:
    print("Error: intents.json not found.")
    intents = []

def get_response(user_input):
    user_input = user_input.lower()
    
    # 1. Rule-based matching (Simple keyword match)
    # Iterate through intents
    for intent in intents:
        for pattern in intent['patterns']:
            # Basic matching: check if pattern is in user input
            if pattern.lower() in user_input:
                return random.choice(intent['responses'])
    
    # 2. AI Fallback
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            # Build context from intents
            context = "School Information:\n"
            for intent in intents:
                context += f"- Topic: {intent['tag']}. Info: {intent['responses'][0]}\n"

            # Create prompt with system context
            prompt = f"System: Use the following School Information to answer the user query. Answer concisely. If information is not available, Provide contact details.\n{context}\nUser: {user_input}"
            
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=prompt
            )
            return response.text
        else:
            return "I'm sorry, I don't understand that. (AI mode not configured)"
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "I'm sorry, I am having trouble connecting to my brain right now."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form.get("msg")
    if not user_input:
        return jsonify({"response": "Please say something."})
    
    response_text = get_response(user_input)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
