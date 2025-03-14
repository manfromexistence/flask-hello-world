from flask import Flask, request, jsonify
from flask_cors import CORS
from main import generate_response
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Check if GEMINI_API_KEY is set
if not os.environ.get("GEMINI_API_KEY"):
    raise ValueError("GEMINI_API_KEY environment variable is not set")

@app.route('/')
def home():
    return jsonify({
        'status': 'ok',
        'message': 'API is running'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'ok',
        'api_key_set': bool(os.environ.get("GEMINI_API_KEY"))
    })

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Question is required'}), 400
        
        model = data.get('model')
        response = generate_response(data['question'], model)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))