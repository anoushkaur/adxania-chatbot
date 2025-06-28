from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    reply = chat_completion.choices[0].message.content
    return jsonify({'response': reply})

@app.route('/')
def home():
    return 'ADXANIA Chatbot is running!'

if __name__ == '__main__':
    app.run(debug=True)
