import os
import uuid
from flask import jsonify, request
from google.cloud import storage


def register(app):
    def upload_file():
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        unique_id = str(uuid.uuid4())
        final_name = f"{unique_id}_{file.filename}"

        client = storage.Client()
        bucket = client.bucket(os.environ.get("GCP_BUCKET_NAME", "learn_microservices"))
        blob = bucket.blob(final_name)
        blob.upload_from_file(file)

        return jsonify(
            {
                "message": "File uploaded successfully",
                "document_name": final_name,
                "document_url": blob.public_url,
            }
        ), 201

    app.add_url_rule("/upload", view_func=upload_file, methods=["POST"])
