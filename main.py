import os
from flask import Flask
from services.rest_sum_service import register as register_rest_sum
from services.rest_register_service import register as register_rest_register
from services.rest_upload_service import register as register_rest_upload
from services.soap_gateway import register as register_soap_gateway

app = Flask(__name__)

register_rest_sum(app)
register_rest_register(app)
register_rest_upload(app)
register_soap_gateway(app)


    



if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
