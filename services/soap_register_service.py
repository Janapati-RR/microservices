import uuid
from .soap_utils import SERVICE_NS, first_text, qname, soap_fault, soap_response


def handle(operation):
    name = first_text(operation, qname(SERVICE_NS, "name"))
    age = first_text(operation, qname(SERVICE_NS, "age"))
    phone = first_text(operation, qname(SERVICE_NS, "phone"))

    if not all([name, age, phone]):
        return soap_fault("Missing name, age, or phone.")

    unique_id = str(uuid.uuid4())
    return soap_response(
        "RegisterResponse",
        {"message": "User registered successfully", "id": unique_id},
        status_code=201,
    )
