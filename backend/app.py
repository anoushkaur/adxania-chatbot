from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    print("Received data:", data)  # For debugging

    user_input = data.get('message', '')
    if not user_input:
        return jsonify({'response': "I didn't receive any message."}), 400

    tone = data.get('tone', 'Neutral')  # Safe default
    response = f"You said: {user_input} (Tone: {tone})"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
