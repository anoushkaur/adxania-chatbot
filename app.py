from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

# Correct way with openai>=1.0.0
client = OpenAI()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    tone = request.json.get('tone', 'professional')

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Respond in a {tone} tone."},
                {"role": "user", "content": user_input}
            ]
        )
        bot_response = completion.choices[0].message.content
        return jsonify({'response': bot_response})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'response': "Sorry, there was an error generating a reply."}), 500

if __name__ == '__main__':
    app.run(debug=True)
