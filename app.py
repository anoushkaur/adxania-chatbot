from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

# Load your OpenAI key from environment variable
client = OpenAI()  # Do NOT pass api_key=... anymore

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    # Call OpenAI's chat endpoint
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({'response': reply})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
