from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

# Set OpenAI API key (expects environment variable to be set in Render)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/', methods=['GET'])
def index():
    return "Adxania Chatbot backend is running.", 200

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    tone = request.json.get('tone', 'professional')

    try:
        prompt = f"Respond to the following in a {tone} tone:\n{user_input}"
        response = openai.Completion.create(
            engine="text-davinci-003",  # use text-davinci-003 for openai==0.28
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        bot_reply = response.choices[0].text.strip()
        return jsonify({'response': bot_reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'response': "Sorry, there was an error generating a reply."}), 500

if __name__ == '__main__':
    app.run(debug=True)
