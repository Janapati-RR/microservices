import os
import uuid
import datetime
from flask import Flask, request, jsonify
from google.cloud import storage

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

# -- POST Service to Accept Attachment as Request and Send Document ID in Response ---

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    To test in Postman:
    1. Body > form-data
    2. Key: 'file' (change type to 'File'), Value: [Select your file]
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400  
    
    unique_id = str(uuid.uuid4())

    # Initialize GCP Storage Client
    client = storage.Client()
    bucket = client.bucket(os.environ.get("GCP_BUCKET_NAME", "learn_microservices"))
    blob = bucket.blob(f"{unique_id}_{file.filename}")
    blob.upload_from_file(file)
    # Get Public URL
    public_url = blob.public_url
    signed_url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=15),
        method="GET",
    )

    print(public_url)
    print(signed_url)


    return jsonify({
        "message": "File uploaded successfully",
        "document_name": f"{unique_id}_{file.filename}",
        "document_url": public_url,
        "document_signed_url": signed_url
    }), 201



if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
