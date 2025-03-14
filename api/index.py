from flask import Flask, request, jsonify
from flask_cors import CORS
from main import generate_response

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/api/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Question is required'}), 400
    
    model = data.get('model')  # Get model if provided
    response = generate_response(data['question'], model)
    return jsonify(response)