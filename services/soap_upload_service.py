import base64
import os
import uuid
from google.cloud import storage
from .soap_utils import SERVICE_NS, first_text, qname, soap_fault, soap_response


def handle(operation):
    filename = first_text(operation, qname(SERVICE_NS, "fileName"))
    file_content = first_text(operation, qname(SERVICE_NS, "fileContent"))

    if not filename or not file_content:
        return soap_fault("Missing fileName or fileContent.")

    try:
        file_bytes = base64.b64decode(file_content, validate=True)
    except ValueError:
        return soap_fault("Invalid Base64 content for fileContent.")

    unique_id = str(uuid.uuid4())
    final_name = f"{unique_id}_{filename}"

    client = storage.Client()
    bucket = client.bucket(os.environ.get("GCP_BUCKET_NAME", "learn_microservices"))
    blob = bucket.blob(final_name)
    blob.upload_from_string(file_bytes)

    return soap_response(
        "UploadResponse",
        {
            "message": "File uploaded successfully",
            "document_name": final_name,
            "document_url": blob.public_url,
        },
        status_code=201,
    )
