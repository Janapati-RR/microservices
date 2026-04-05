import os
import base64
from flask import jsonify
from google.cloud import storage

def register(app):
    def fetch_excel():
        try:
            # Initialize the GCS client
            client = storage.Client()
            
            # Hardcoded bucket and filename as requested
            bucket_name = "pyproject-rj123-bucket"
            blob_name = "10mb.xlsx"
            
            bucket = client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            
            # Download the document as bytes
            file_bytes = blob.download_as_bytes()
            
            # Encode bytes to base64
            encoded_data = base64.b64encode(file_bytes).decode('utf-8')
            
            return jsonify({
                "message": "File fetched successfully",
                "filename": blob_name,
                "document_data": encoded_data
            }), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    app.add_url_rule("/fetch-excel", view_func=fetch_excel, methods=["POST"])
