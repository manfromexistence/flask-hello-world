import requests
import argparse
import json

def ask_question(question):
    url = 'http://localhost:5000/api/ask'
    headers = {'Content-Type': 'application/json'}
    data = {'question': question}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        # Format the response to remove extra newlines and clean up whitespace
        formatted_response = ' '.join(result['response'].split())
        print("\nAI Response:", formatted_response)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def interactive_mode():
    print("AI Chat CLI (Press Ctrl+C to exit)")
    print("--------------------------------")
    
    try:
        while True:
            question = input("\nYour question: ")
            if question.strip():
                ask_question(question)
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI tool to interact with AI API")
    parser.add_argument("--question", "-q", help="Ask a single question and exit")
    
    args = parser.parse_args()
    
    if args.question:
        ask_question(args.question)
    else:
        interactive_mode()