import defusedxml.ElementTree as safe_et
from flask import Response, request
from .soap_register_service import handle as handle_register
from .soap_sum_service import handle as handle_sum
from .soap_upload_service import handle as handle_upload
from .soap_utils import SOAP_NS, qname, soap_fault
from .soap_wsdl import build_wsdl


def register(app):
    def soap_service():
        if request.method == "GET":
            if "wsdl" in request.args:
                wsdl_xml = build_wsdl(request.base_url)
                return Response(wsdl_xml, status=200, mimetype="text/xml")
            return Response(
                "Use POST /soap for SOAP calls or GET /soap?wsdl for contract.",
                status=200,
                mimetype="text/plain",
            )

        try:
            envelope = safe_et.fromstring(request.data or b"")
        except safe_et.ParseError:
            return soap_fault("Invalid XML payload.")

        body = envelope.find(qname(SOAP_NS, "Body"))
        if body is None or len(body) == 0:
            return soap_fault("SOAP Body is missing.")

        operation = body[0]
        operation_name = operation.tag.split("}", 1)[-1]

        if operation_name == "SumRequest":
            return handle_sum(operation)
        if operation_name == "RegisterRequest":
            return handle_register(operation)
        if operation_name == "UploadRequest":
            return handle_upload(operation)
        return soap_fault(f"Unsupported operation: {operation_name}")

    app.add_url_rule("/soap", view_func=soap_service, methods=["GET", "POST"])
