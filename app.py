import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

openai.api_key = "your-openai-api-key-here"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    tone = request.json.get('tone', 'neutral')

    prompt = f"Reply in a {tone} tone to: {user_input}"

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        bot_reply = completion.choices[0].message.content
        return jsonify({'response': bot_reply})
    except Exception as e:
        return jsonify({'response': f"Error: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
