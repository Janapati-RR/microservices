import os
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- GET SERVICE (Sum of 2 numbers) ---
@app.route('/sum', methods=['GET'])
def add_numbers():
    # Get numbers from request parameters (e.g., /sum?num1=5&num2=10)
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({"result": num1 + num2}), 200
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers."}), 400

# --- POST SERVICE (User Registration) ---
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
        
    name = data.get('name')
    age = data.get('age')
    phone = data.get('phone')

    if not all([name, age, phone]):
        return jsonify({"error": "Missing name, age, or phone"}), 400

    unique_id = str(uuid.uuid4())
    return jsonify({
        "message": "User registered successfully",
        "id": unique_id
    }), 201

if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
