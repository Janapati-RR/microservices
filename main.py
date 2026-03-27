import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def add_numbers():
    # Get numbers from request parameters (e.g., /sum?num1=5&num2=10)
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        return jsonify({"result": num1 + num2}), 200
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers."}), 400

if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
