from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

# Use the environment variable for the API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    tone = request.json.get('tone', 'professional')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are Adxania, a smart, friendly AI assistant from an AI chatbot product company. "
                        f"You help businesses automate customer service through website and WhatsApp chatbots. "
                        f"Your services include: custom chatbot development, multilingual support, lead generation, "
                        f"analytics, integration with CRM tools, and continuous optimization. Respond in a {tone} tone, "
                        f"and always stay on brand, sounding helpful, modern, and confident."
                    )
                },
                {"role": "user", "content": user_input}
            ]
        )
        bot_reply = response['choices'][0]['message']['content']
        return jsonify({'response': bot_reply})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'response': "Sorry, there was an error generating a reply."}), 500

if __name__ == '__main__':
    app.run(debug=True)
