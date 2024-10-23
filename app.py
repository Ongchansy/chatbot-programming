from flask import Flask, request, jsonify, render_template
from chatbot_model import get_response  # Import chatbot response logic

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')  # Renders a simple frontend to interact with the bot

# Route to handle chatbot communication
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")  # Get the user input from the frontend
    if not user_input:
        return jsonify({"error": "No message received"}), 400

    response = get_response(user_input)  # Get chatbot's response
    return jsonify({"response": response})  # Return the response as JSON

if __name__ == "__main__":
    app.run(debug=True)
