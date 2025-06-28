from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    tone = request.json.get('tone', 'professional')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Respond in a {tone} tone, based on Adxania's services."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        bot_response = response['choices'][0]['message']['content']
        return jsonify({'response': bot_response})
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'response': "Sorry, there was an error generating a reply."}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
