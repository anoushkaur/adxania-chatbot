from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="https://anoushkaur.github.io")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    tone = request.json.get('tone', 'professional')
    response = f"You said: {user_input} (Tone: {tone})"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
