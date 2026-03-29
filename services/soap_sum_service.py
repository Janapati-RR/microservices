from .soap_utils import SERVICE_NS, first_text, qname, soap_fault, soap_response


def handle(operation):
    try:
        num1 = float(first_text(operation, qname(SERVICE_NS, "num1")))
        num2 = float(first_text(operation, qname(SERVICE_NS, "num2")))
    except ValueError:
        return soap_fault("Invalid input. Please provide numbers.")

    return soap_response("SumResponse", {"result": num1 + num2})
